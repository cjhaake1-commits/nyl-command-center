from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Iterable, Mapping


STAGE_WEIGHTS = {
    "New": 4,
    "Attempting contact": 8,
    "Connected": 12,
    "Appointment set": 18,
    "Appointment held": 20,
    "Proposal / follow-up": 16,
    "Won": 0,
    "Lost": 0,
    "Nurture": 5,
}


@dataclass(frozen=True)
class LeadSourcePlaybook:
    source: str
    description: str
    best_for: tuple[str, ...]
    actions: tuple[str, ...]
    quality: int
    speed: int


LEAD_SOURCE_PLAYBOOKS = (
    LeadSourcePlaybook(
        source="Warm network & introductions",
        description="People you already know plus introductions from people who know and trust you.",
        best_for=("Broad market", "Professionals", "Business owners"),
        actions=(
            "List 25 people you can contact personally without scraping a platform.",
            "Ask each quality conversation for one or two permission-based introductions.",
            "Record the introducer as the source so referral conversion can be measured.",
        ),
        quality=5,
        speed=5,
    ),
    LeadSourcePlaybook(
        source="Centers of influence",
        description="Build reciprocal relationships with professionals who regularly meet people needing financial guidance.",
        best_for=("Business owners", "Professionals", "Broad market"),
        actions=(
            "Build a target list of CPAs, attorneys, mortgage professionals, real-estate professionals, and business advisers.",
            "Use public business contact information or approved introductions.",
            "Track each relationship separately from end-client prospects.",
        ),
        quality=5,
        speed=3,
    ),
    LeadSourcePlaybook(
        source="Local business prospecting",
        description="Identify local businesses through public business directories, chambers, and association listings.",
        best_for=("Business owners", "Professionals"),
        actions=(
            "Search public business directories for the selected industry and geography.",
            "Capture the business name, public business contact route, and why it fits your target market.",
            "Do not infer sensitive personal information; qualify through conversation instead.",
        ),
        quality=4,
        speed=4,
    ),
    LeadSourcePlaybook(
        source="Professional & community groups",
        description="Create repeatable prospecting opportunities through groups where participation is permitted.",
        best_for=("Professionals", "Business owners", "Broad market"),
        actions=(
            "List chambers, trade groups, alumni groups, volunteer groups, and professional associations relevant to your market.",
            "Prioritize events with recurring attendance so relationships can compound over time.",
            "Use the organization's rules and approved contact practices rather than scraping member lists.",
        ),
        quality=4,
        speed=3,
    ),
    LeadSourcePlaybook(
        source="Referral partners",
        description="Create a deliberate cadence with people who can make qualified introductions.",
        best_for=("Business owners", "Professionals", "Broad market"),
        actions=(
            "Identify 10 potential referral partners with complementary client relationships.",
            "Prepare a short explanation of who you help and what a good introduction looks like.",
            "Track introductions and outcomes by partner to find the highest-converting relationships.",
        ),
        quality=5,
        speed=3,
    ),
    LeadSourcePlaybook(
        source="Approved events & seminars",
        description="Use company-approved educational or community events to create opt-in conversations.",
        best_for=("Broad market", "Professionals", "Business owners"),
        actions=(
            "Choose a narrowly defined audience and useful educational topic.",
            "Use only approved invitations, materials, disclosures, and follow-up workflows.",
            "Capture only people who affirmatively opt in to follow-up.",
        ),
        quality=4,
        speed=2,
    ),
)


def lead_source_plan(segment: str, target_new_leads: int) -> list[dict]:
    """Rank lead-source playbooks for a target segment and allocate a practical lead mission."""
    target = max(1, int(target_new_leads))
    ranked = sorted(
        LEAD_SOURCE_PLAYBOOKS,
        key=lambda p: ((segment in p.best_for), p.quality, p.speed),
        reverse=True,
    )
    weights = [max(1, p.quality + p.speed) for p in ranked[:4]]
    total_weight = sum(weights)

    rows: list[dict] = []
    assigned = 0
    for index, (playbook, weight) in enumerate(zip(ranked[:4], weights)):
        if index == len(weights) - 1:
            allocation = max(0, target - assigned)
        else:
            allocation = round(target * weight / total_weight)
            assigned += allocation
        rows.append(
            {
                "Source": playbook.source,
                "Lead target": allocation,
                "Quality": playbook.quality,
                "Speed": playbook.speed,
                "Why": playbook.description,
                "Actions": " | ".join(playbook.actions),
            }
        )
    return rows


def priority_score(prospect: Mapping, today: date | None = None) -> int:
    """Score next-best-action priority using non-sensitive, user-entered sales factors."""
    today = today or date.today()
    if bool(prospect.get("do_not_contact", False)):
        return -1000
    if str(prospect.get("stage", "")) in {"Won", "Lost"}:
        return -100

    fit = max(1, min(5, int(prospect.get("fit_score", 3) or 3)))
    warmth = max(1, min(5, int(prospect.get("warmth_score", 3) or 3)))
    urgency = max(1, min(5, int(prospect.get("urgency_score", 3) or 3)))
    source_quality = max(1, min(5, int(prospect.get("source_quality", 3) or 3)))
    stage = str(prospect.get("stage", "New") or "New")

    score = fit * 6 + warmth * 5 + urgency * 5 + source_quality * 3
    score += STAGE_WEIGHTS.get(stage, 4)

    next_action_date = prospect.get("next_action_date")
    if next_action_date:
        try:
            due = datetime.fromisoformat(str(next_action_date)).date()
            delta = (due - today).days
            if delta < 0:
                score += 24
            elif delta == 0:
                score += 20
            elif delta <= 2:
                score += 12
            elif delta <= 7:
                score += 5
        except ValueError:
            pass

    last_contact = prospect.get("last_contact_date")
    if last_contact:
        try:
            last = datetime.fromisoformat(str(last_contact)).date()
            days_since = max(0, (today - last).days)
            score += min(12, days_since // 3)
        except ValueError:
            pass
    else:
        score += 8

    consent_status = str(prospect.get("consent_status", "Unknown") or "Unknown")
    if consent_status == "Permission / existing relationship":
        score += 6
    elif consent_status == "Do not contact":
        return -1000

    return int(score)


def ranked_prospects(prospects: Iterable[Mapping], today: date | None = None) -> list[dict]:
    rows = []
    for prospect in prospects:
        row = dict(prospect)
        row["priority_score"] = priority_score(row, today=today)
        rows.append(row)
    return sorted(rows, key=lambda r: r["priority_score"], reverse=True)


def prospecting_gap(daily_outreach_target: int, active_prospects: int, coverage_multiple: int = 3) -> int:
    """Estimate how many additional pipeline names are useful to support today's outreach mission."""
    desired = max(0, int(daily_outreach_target)) * max(1, int(coverage_multiple))
    return max(0, desired - max(0, int(active_prospects)))
