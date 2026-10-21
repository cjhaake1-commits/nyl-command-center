from __future__ import annotations

from datetime import date, datetime
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from data.db import get_activity, init_db, persistent_storage_enabled, storage_backend
from data.prospects import get_prospects, init_prospect_db

st.set_page_config(page_title="Relationship Quarterback | Chris Haake", page_icon="🏈", layout="wide")
init_db()
init_prospect_db()
brand_hero(
    "Relationship Quarterback",
    "One focused view of the next best work: protect active relationships, follow up on referrals, and make each week measurable.",
    "Chris Haake • New York Life",
)

today = datetime.now(ZoneInfo("America/New_York")).date()
st.caption(f"{today:%A, %B %d, %Y} • Daily operating view")
if not persistent_storage_enabled():
    st.warning(f"Activity storage is {storage_backend()}. Existing prospect data and activity may not persist across restarts; verify database status before relying on saved history.")

st.info("This is a workflow prioritizer, not a client recommendation engine. Do not add client-identifying or confidential information here. Keep official records and client-specific work in approved NYL systems.")

prospects = get_prospects()
activity = get_activity()

def _date_value(value):
    try:
        return date.fromisoformat(str(value)[:10])
    except (TypeError, ValueError):
        return None

def _days_since(value):
    d = _date_value(value)
    return (today - d).days if d else None

def _safe_stage(row):
    return str(row.get("stage", "New") or "New").strip()

def _priority(row):
    stage = _safe_stage(row).lower()
    next_date = _date_value(row.get("next_action_date"))
    overdue = bool(next_date and next_date < today)
    no_action = not str(row.get("next_action", "") or "").strip() or not next_date
    touch_age = _days_since(row.get("last_contact_date"))
    if overdue:
        return 0, "Overdue next action"
    if no_action:
        return 1, "No dated next action"
    if stage in {"active opportunity", "meeting scheduled", "proposal", "application"}:
        return 2, "Active relationship"
    if touch_age is not None and touch_age >= 14 and stage not in {"closed", "not a fit", "do not contact"}:
        return 3, "Reconfirm next step"
    return 4, "On track"

def _source(row):
    return str(row.get("source", "") or "Unspecified")

st.subheader("Today’s attention queue")
priority_rows = []
for row in prospects:
    rank, reason = _priority(row)
    if rank < 4:
        priority_rows.append({
            "Priority": rank,
            "Reason": reason,
            "Subject": row.get("organization") or row.get("prospect_name") or "Unnamed record",
            "Stage": _safe_stage(row),
            "Next action": row.get("next_action") or "Set a concrete, permission-based next action",
            "Due": row.get("next_action_date") or "Not set",
            "Source": _source(row),
        })
priority_rows.sort(key=lambda x: (x["Priority"], str(x["Due"])))
if priority_rows:
    st.dataframe(pd.DataFrame(priority_rows), width="stretch", hide_index=True, column_config={"Priority": st.column_config.NumberColumn(format="%d")})
else:
    st.success("No overdue or incomplete follow-up records in the saved pipeline. Use the next block to develop qualified conversations and referral relationships.")
st.caption("The queue prioritizes due dates and explicit stages; it does not score a person's wealth, need, or suitability.")

c1, c2, c3, c4 = st.columns(4)
overdue = sum(1 for row in prospects if (_date_value(row.get("next_action_date")) or today) < today)
no_dated_action = sum(1 for row in prospects if not row.get("next_action") or not row.get("next_action_date"))
warm = sum(1 for row in prospects if _safe_stage(row).lower() in {"active opportunity", "meeting scheduled", "proposal", "application"})
c1.metric("Pipeline records", len(prospects))
c2.metric("Overdue", overdue)
c3.metric("Missing next action/date", no_dated_action)
c4.metric("Active opportunities", warm)

st.divider()
st.subheader("Referral engine • source to outcome")
st.caption("Track relationship sources by aggregate stage outcomes. Keep names and client details in approved systems.")
source_rows = []
source_names = sorted({_source(row) for row in prospects})
for source in source_names:
    group = [row for row in prospects if _source(row) == source]
    source_rows.append({
        "Source": source,
        "Records": len(group),
        "Meetings / active": sum(1 for row in group if _safe_stage(row).lower() in {"meeting scheduled", "active opportunity", "proposal", "application"}),
        "Placed / won": sum(1 for row in group if _safe_stage(row).lower() in {"won", "placed", "closed won"}),
        "Unworked": sum(1 for row in group if not row.get("next_action") or not row.get("next_action_date")),
    })
if source_rows:
    st.dataframe(pd.DataFrame(source_rows).sort_values(["Records", "Meetings / active"], ascending=False), width="stretch", hide_index=True)
else:
    st.info("As source records accumulate in the approved pipeline, this will show which relationship channels produce qualified conversations and follow-through.")
st.markdown("**Referral follow-up rhythm**")
rhythm = [
    {"When": "Same day", "Action": "Thank the connector, confirm permission and the preferred introduction path; log the source in the approved system."},
    {"When": "Within 1 business day", "Action": "Respond to the referred person with context and a simple, low-pressure next step."},
    {"When": "After first conversation", "Action": "Close the loop with the connector only when the referred person has authorized it; protect confidentiality."},
    {"When": "Weekly", "Action": "Review introductions received, introductions requested with permission, meetings held, and source-to-meeting conversion."},
]
st.dataframe(pd.DataFrame(rhythm), width="stretch", hide_index=True)

st.divider()
st.subheader("Sales activity scorecard")
week_start = today - timedelta(days=today.weekday())
week_rows = [row for row in activity if week_start.isoformat() <= str(row.get("activity_date", "")) <= today.isoformat()]
week_totals = {
    "Outreach": sum(int(row.get("outreach_attempts", 0) or 0) for row in week_rows),
    "Conversations": sum(int(row.get("conversations", 0) or 0) for row in week_rows),
    "Appointments booked": sum(int(row.get("appointments_booked", 0) or 0) for row in week_rows),
    "Appointments held": sum(int(row.get("appointments_held", 0) or 0) for row in week_rows),
    "Sales logged": sum(int(row.get("sales", 0) or 0) for row in week_rows),
    "Commission logged": sum(float(row.get("commission", 0) or 0) for row in week_rows),
}
cols = st.columns(6)
for col, (label, value) in zip(cols, week_totals.items()):
    col.metric(label, f"$" + f"{value:,.0f}" if label == "Commission logged" else f"{value:,}")
st.caption(f"Week of Monday {week_start:%B %d, %Y}. Activity and commission values are manually entered; reconcile production with NYL’s official reports.")

st.divider()
st.subheader("Monday coach prompt")
with st.form("quarterback_monday_review"):
    goal = st.text_input("One measurable outcome for the week", placeholder="Example: 6 qualified meetings held")
    focus = st.selectbox("Main focus", ["Protect active cases", "Warm introductions", "Business-owner relationships", "Professional referral partners", "Retirement-transition conversations", "Improve meeting-to-next-step conversion"])
    friction = st.selectbox("Main friction to solve", ["Insufficient qualified conversations", "Low show rate", "Slow case follow-through", "Unclear referral path", "Weak next-step commitment", "Need manager or specialist guidance", "Other"])
    manager_needed = st.checkbox("This needs manager / compliance / appointed specialist input")
    saved = st.form_submit_button("Create my weekly commitment", type="primary")
if saved:
    st.session_state["quarterback_commitment"] = {
        "week": week_start.isoformat(),
        "outcome": goal.strip(),
        "focus": focus,
        "friction": friction,
        "escalate": manager_needed,
    }
    st.success("Weekly commitment saved in this browser session.")
commitment = st.session_state.get("quarterback_commitment")
if commitment and commitment.get("week") == week_start.isoformat():
    st.markdown(f"**Commitment:** {commitment['outcome'] or 'Set a specific measurable outcome'} · **Focus:** {commitment['focus']} · **Friction:** {commitment['friction']}")
    if commitment["escalate"]:
        st.warning("Bring this to the right manager, compliance contact, or appointed specialist before acting on any policy, compensation, licensing, suitability, product-access, or client-specific question.")

st.divider()
st.subheader("Operating rules for a durable seven-figure practice")
st.markdown("- Build around a few repeatable referral ecosystems, then measure source-to-meeting and meeting-to-placed outcomes.\n- Give every active opportunity a dated next action; clear stale items each week.\n- Protect case service and persistency; paid/credited production is the scoreboard, while premium, assets and submitted applications are not substitutes.\n- Balance business-owner and professional relationships with individual protection, retirement and investment conversations only when discovery supports them.\n- Use group benefits, advanced planning, or securities specialists through approved referral and case-credit pathways.\n- Treat the $1M goal as a stretch operating target. Validate credited commission economics, capacity, persistency and licensing with field leadership.")
st.page_link("pages/17_First_Year_Growth_Plan.py", label="Review the First-Year Growth Plan", icon="🏆")
st.page_link("pages/19_Sales_Coach.py", label="Open Sales Coach", icon="🧭")
