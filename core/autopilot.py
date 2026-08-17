from __future__ import annotations

from datetime import date, datetime
from typing import Iterable, Mapping

from core.prospecting import priority_score

ACTIVE_STAGES = {"New", "Attempting contact", "Connected", "Needs identified", "Appointment set", "Follow-up"}


def _parse_date(value: object) -> date | None:
    if not value:
        return None
    try:
        return datetime.strptime(str(value)[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def pipeline_hygiene(prospects: Iterable[Mapping[str, object]], today: date | None = None) -> dict:
    today = today or date.today()
    no_next_date = 0
    overdue = 0
    due_today = 0
    active = 0
    dnc_active = 0
    for p in prospects:
        stage = str(p.get("stage") or "New")
        if stage not in ACTIVE_STAGES:
            continue
        active += 1
        if bool(p.get("do_not_contact")) or str(p.get("consent_status") or "") == "Do not contact":
            dnc_active += 1
            continue
        due = _parse_date(p.get("next_action_date"))
        if not due:
            no_next_date += 1
        elif due < today:
            overdue += 1
        elif due == today:
            due_today += 1
    return {
        "active": active,
        "no_next_date": no_next_date,
        "overdue": overdue,
        "due_today": due_today,
        "dnc_active": dnc_active,
        "clean_pct": round(100.0 * max(0, active - no_next_date - overdue - dnc_active) / active, 1) if active else 100.0,
    }


def build_action_queue(
    prospects: Iterable[Mapping[str, object]],
    touchpoints: Iterable[Mapping[str, object]],
    today: date | None = None,
    limit: int = 20,
) -> list[dict]:
    today = today or date.today()
    inbound_followups: dict[int, int] = {}
    for t in touchpoints:
        try:
            pid = int(t.get("prospect_id") or 0)
        except (TypeError, ValueError):
            continue
        if not pid:
            continue
        if str(t.get("direction") or "") == "inbound" and bool(t.get("requires_follow_up")):
            inbound_followups[pid] = inbound_followups.get(pid, 0) + 1

    queue: list[dict] = []
    for p in prospects:
        stage = str(p.get("stage") or "New")
        if stage not in ACTIVE_STAGES:
            continue
        if bool(p.get("do_not_contact")) or str(p.get("consent_status") or "") == "Do not contact":
            continue

        try:
            pid = int(p.get("id") or 0)
        except (TypeError, ValueError):
            pid = 0

        score = max(0.0, float(priority_score(p, today=today)))
        reason_parts: list[str] = []
        recommended = str(p.get("next_action") or "Human review / assign next action")
        due = _parse_date(p.get("next_action_date"))

        if inbound_followups.get(pid, 0):
            score += 120
            reason_parts.append("Inbound reply needs follow-up")
            recommended = "Respond personally and pause any remaining sequence"

        if due is None:
            score += 75
            reason_parts.append("No dated next action")
            recommended = "Assign a specific next action and date"
        else:
            delta = (due - today).days
            if delta < 0:
                score += min(100, 70 + abs(delta) * 3)
                reason_parts.append(f"Overdue by {abs(delta)} day(s)")
            elif delta == 0:
                score += 65
                reason_parts.append("Due today")
            elif delta <= 2:
                score += 30
                reason_parts.append("Due within 48 hours")

        if stage == "Appointment set":
            score += 35
            reason_parts.append("Meeting booked")
            if not recommended:
                recommended = "Prepare meeting brief and desired next decision"
        elif stage == "Needs identified":
            score += 25
            reason_parts.append("Diagnostic-stage momentum")

        if str(p.get("consent_status") or "") == "Existing relationship":
            score += 15
            reason_parts.append("Existing relationship")

        queue.append({
            "prospect_id": pid,
            "name": str(p.get("prospect_name") or ""),
            "organization": str(p.get("organization") or ""),
            "stage": stage,
            "score": round(score, 1),
            "reason": "; ".join(reason_parts) if reason_parts else "Priority score / planned follow-up",
            "recommended_action": recommended,
            "due": str(p.get("next_action_date") or ""),
            "source": str(p.get("source") or ""),
        })

    queue.sort(key=lambda x: x["score"], reverse=True)
    return queue[: max(1, int(limit))]


def sequence_recommendation(prospect: Mapping[str, object], touch_count: int) -> dict:
    segment = str(prospect.get("market_segment") or "").lower()
    source = str(prospect.get("source") or "").lower()

    if "center of influence" in segment or "referral" in source:
        sequence = "COI 20-Day"
        steps = [
            (0, "Research niche, clients, affiliations and one complementary issue"),
            (1, "Request a 20-minute professional-to-professional conversation"),
            (2, "Phone follow-up and propose two times"),
            (3, "Engage through LinkedIn/shared event if approved"),
            (4, "Share one approved useful resource or co-host idea"),
            (5, "Propose one small joint education test or relevant introduction"),
        ]
    elif "event" in source or "network" in source:
        sequence = "Event 10-Day"
        steps = [
            (0, "Capture the specific event topic and agreed follow-up"),
            (1, "Send a specific note within 24 hours and propose two times"),
            (2, "Ask one follow-up question by phone/LinkedIn"),
            (3, "Send one approved relevant resource or invite"),
            (4, "Close the loop or schedule; no perpetual networking limbo"),
        ]
    else:
        sequence = "Owner 14-Day"
        steps = [
            (0, "Verify one public trigger and one relevant owner-level question"),
            (1, "Send a short trigger-based email and 20-minute ask"),
            (2, "Make a concise phone call through an approved channel"),
            (3, "Use contextual LinkedIn engagement if approved"),
            (4, "Send one approved checklist or event invite"),
            (5, "Second call tied to the same issue or a new public fact"),
            (6, "Close-loop message; recycle only on a new trigger"),
        ]

    idx = min(max(0, int(touch_count)), len(steps) - 1)
    return {"sequence": sequence, "step_index": idx, "recommended_action": steps[idx][1]}


def first_100_progress(prospects: Iterable[Mapping[str, object]]) -> list[dict]:
    buckets = [
        ("Owner-led growth companies", 40, {"business owner", "corporation"}),
        ("Medical / professional practice owners", 20, {"professional"}),
        ("Centers of influence", 20, {"center of influence"}),
        ("Hospitality / construction / real-estate operators", 10, {"real-estate investor"}),
        ("Established executives / technical professionals", 10, {"executive"}),
    ]
    raw = [str(p.get("market_segment") or "").strip().lower() for p in prospects]
    rows: list[dict] = []
    for label, target, tags in buckets:
        current = sum(1 for segment in raw if segment in tags)
        rows.append({
            "segment": label,
            "target": target,
            "current_approx": current,
            "gap": max(0, target - current),
            "progress_pct": round(min(100.0, current / target * 100.0), 1) if target else 100.0,
        })
    return rows
