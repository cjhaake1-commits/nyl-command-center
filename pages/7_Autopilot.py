from __future__ import annotations

import pandas as pd
import streamlit as st

from core.autopilot import build_action_queue, first_100_progress, pipeline_hygiene, sequence_recommendation
from data.prospects import get_prospects, get_touchpoints, init_prospect_db

st.set_page_config(page_title="NYL Autopilot", page_icon="⚡", layout="wide")
init_prospect_db()

st.title("Sales Autopilot")
st.caption("Internal execution assistant: prioritize work, close open loops, and recommend the next task. No external messages are auto-sent.")

st.warning(
    "Autopilot is intentionally internal-only until NYL approves the exact CRM, communication, AI and workflow rules. "
    "It can rank, remind, prepare and report; human review controls all outreach and recommendations."
)

prospects = get_prospects()
touches = get_touchpoints(limit=500)

hygiene = pipeline_hygiene(prospects)
h1, h2, h3, h4, h5 = st.columns(5)
h1.metric("Active records", hygiene["active"])
h2.metric("Overdue", hygiene["overdue"])
h3.metric("No next date", hygiene["no_next_date"])
h4.metric("Due today", hygiene["due_today"])
h5.metric("Pipeline hygiene", f"{hygiene['clean_pct']:.0f}%")

if hygiene["no_next_date"] or hygiene["overdue"]:
    st.warning("Pipeline truth rule is not yet met: every active record should have a current dated next action.")
else:
    st.success("All active records currently have a current dated next action.")

st.subheader("Today's Autonomous Priority Queue")
queue = build_action_queue(prospects, touches, limit=20)
if queue:
    st.dataframe(pd.DataFrame(queue), width="stretch", hide_index=True)
    top = queue[0]
    st.success(f"Do this first: {top['name']} — {top['recommended_action']} ({top['reason']}).")
else:
    st.info("No active prospect tasks yet. Build the first-100 account universe and assign dated next actions.")

st.subheader("Sequence Coach")
if prospects:
    active = [p for p in prospects if str(p.get("stage") or "") not in {"Won", "Lost"} and not bool(p.get("do_not_contact"))]
    if active:
        labels = {f"#{p['id']} — {p['prospect_name']} / {p.get('organization','')}": p for p in active}
        selected_label = st.selectbox("Prospect", list(labels.keys()))
        selected = labels[selected_label]
        prospect_touches = [t for t in touches if int(t.get("prospect_id") or 0) == int(selected["id"])]
        rec = sequence_recommendation(selected, len(prospect_touches))
        c1, c2, c3 = st.columns(3)
        c1.metric("Recommended sequence", rec["sequence"])
        c2.metric("Logged touches", len(prospect_touches))
        c3.metric("Next sequence step", rec["step_index"] + 1)
        st.info(rec["recommended_action"])
        st.caption("Recommendation only. Verify relevance, approved channel, consent/DNC status, and firm policy before any contact.")

st.subheader("First-100 Coverage Monitor")
coverage = first_100_progress(prospects)
st.dataframe(pd.DataFrame(coverage), width="stretch", hide_index=True)
total_current = sum(int(row["current_approx"]) for row in coverage)
total_gap = sum(int(row["gap"]) for row in coverage)
c1, c2, c3 = st.columns(3)
c1.metric("Mapped toward first 100", total_current)
c2.metric("Remaining gap", total_gap)
c3.metric("Target", 100)

st.subheader("Autonomous Internal Rules")
rules = [
    {"Trigger": "Inbound reply", "Automatic internal action": "Move to top of queue; pause remaining sequence; create response task", "Human action": "Read context and respond personally"},
    {"Trigger": "No dated next action", "Automatic internal action": "Flag record as broken and raise priority", "Human action": "Choose next step and assign date"},
    {"Trigger": "Overdue next action", "Automatic internal action": "Escalate in daily queue", "Human action": "Complete, reschedule with reason, or close"},
    {"Trigger": "Meeting booked", "Automatic internal action": "Raise priority and prepare meeting-brief task", "Human action": "Prepare questions and desired next decision"},
    {"Trigger": "Touch logged", "Automatic internal action": "Refresh recency and recommend next sequence step", "Human action": "Verify relevance before next outreach"},
    {"Trigger": "No response after sequence", "Automatic internal action": "Recommend recycle instead of endless follow-up", "Human action": "Re-engage only with new relevance"},
    {"Trigger": "Client implemented (future Salesforce)", "Automatic internal action": "Create 7/30/90-day and annual review reminders", "Human action": "Deliver service and earn introductions after value"},
]
st.dataframe(pd.DataFrame(rules), width="stretch", hide_index=True)

st.subheader("Future Salesforce Autopilot")
st.write(
    "Once NYL authorizes API/OAuth access, the same engine can read approved Salesforce tasks, activities, replies and relationship fields; "
    "deduplicate imported activity by Salesforce ID; rebuild this queue automatically; and create permitted internal tasks/status updates. "
    "Salesforce remains the official system of record."
)

st.caption("Goal: automate administration and attention management, not judgment, suitability, advice, or client communications.")
