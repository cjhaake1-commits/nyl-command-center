from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from data.db import get_activity, init_db, storage_backend, persistent_storage_enabled
from data.hnw_leads import HNW_LEADS
from data.marketing_network_leads import MARKETING_NETWORK_LEADS
from data.prospects import init_prospect_db, prospect_counts
from data.public_leads import PUBLIC_LEADS

st.set_page_config(page_title="Command Center | Chris Haake", page_icon="◆", layout="wide")
init_db()
init_prospect_db()

brand_hero(
    "Growth Command Center",
    "A practical operating view for Central Florida prospect development, relationship building, production activity, and disciplined follow-through.",
    "Chris Haake • New York Life",
)

business_count = len(PUBLIC_LEADS)
hnw_count = len(HNW_LEADS)
network_count = len(MARKETING_NETWORK_LEADS)
total_discovery = business_count + hnw_count + network_count
high_fit_network = sum(1 for x in MARKETING_NETWORK_LEADS if float(x.get("Audience fit score", 0) or 0) >= 95)
high_hnw = sum(1 for x in HNW_LEADS if float(x.get("Opportunity score", 0) or 0) >= 95)

today = datetime.now(ZoneInfo("America/New_York")).date()
activity_rows = get_activity()
month_start = today.replace(day=1).isoformat()
month_end = today.isoformat()
month_activity = [
    row for row in activity_rows
    if month_start <= str(row.get("activity_date", "")) <= month_end
]
month_commission = sum(float(row.get("commission", 0) or 0) for row in month_activity)
month_sales = sum(int(row.get("sales", 0) or 0) for row in month_activity)
pipeline = prospect_counts()

st.success("COMMAND CENTER • RUNNING")
if persistent_storage_enabled():
    st.success("ACTIVITY STORAGE • PERSISTENT")
else:
    st.warning(
        f"ACTIVITY STORAGE • {storage_backend()} — activity and pipeline records may not persist across app restarts. "
        "Confirm persistent storage before relying on saved history."
    )
st.caption(
    "Prospect catalogs on this page are curated research files, not live data feeds or a Salesforce connection. "
    "Verify source details and current NYL requirements before acting."
)

st.subheader("Executive Snapshot")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Research Candidates", total_discovery, "curated records")
c2.metric("Active Pipeline", int(pipeline.get("active", 0) or 0), "Command Center records")
c3.metric("Sales This Month", month_sales, f"{len(month_activity)} days logged")
c4.metric("Commission Logged This Month", f"${month_commission:,.0f}", "from saved activity")
c5.metric("Referral Network", network_count, f"{high_fit_network} fit 95+")

st.subheader("Growth Priorities")
st.caption("Targets describe the intended operating plan. This prototype does not claim these goals are completed or synced to Salesforce.")
goals = [
    {
        "Goal": "Build a qualified prospect universe",
        "Target": "5,000 validated, net-new leads",
        "Proof": "Count accepted Salesforce Created rows only; deduplicate against existing records and preserve source evidence.",
        "Next action": "Verify identity, business fit, public source, and contact details before approved import or outreach.",
    },
    {
        "Goal": "Build a strong practice ramp",
        "Target": "First 100 qualified accounts, then a consistent weekly rhythm",
        "Proof": "Manager-confirmed 30/60/90-day expectations, approved tools, dated next actions, and weekly activity/conversion review.",
        "Next action": "Align the ramp measures with the manager and use Daily War Room to test editable production assumptions.",
    },
    {
        "Goal": "Earn sponsorship for a focused pilot",
        "Target": "Demonstrate a reviewable Central Florida relationship-development workflow",
        "Proof": "Source quality, follow-through, introductions, meetings, conversion, and clear compliance boundaries.",
        "Next action": "Agree on a small scope and success measures before expanding access, data, or use.",
    },
]
st.dataframe(pd.DataFrame(goals), width="stretch", hide_index=True)
st.caption(
    f"Curated discovery universe: {business_count} business, {hnw_count} HNW/COI, "
    f"and {network_count} referral-network research records. These are research candidates, not validated Salesforce imports."
)

st.subheader("Operating Priorities")
cols = st.columns(3)
with cols[0]:
    st.markdown("### 01 • Build qualified pipeline")
    st.write(
        f"{int(pipeline.get('active', 0) or 0)} active records are currently in the local pipeline. "
        "Prioritize source verification, a credible warm path, permission-based outreach, and a dated next action."
    )
with cols[1]:
    st.markdown("### 02 • Develop durable relationships")
    st.write(
        "Build professional and community relationships with COIs, business owners, employers, and local organizations. "
        "Track introductions and follow-up; do not treat audience fit or public career signals as evidence of private need."
    )
with cols[2]:
    st.markdown("### 03 • Improve execution")
    st.write(
        f"{len(month_activity)} activity dates have been logged this month, with {month_sales} placed sales recorded. "
        "Review the funnel and weakest conversion step in Daily War Room, then adjust the next week's activity."
    )

st.subheader("Growth Flywheel")
cols = st.columns(4)
modules = [
    ("01", "Discover", "Public signals, referrals, events, and professional relationships"),
    ("02", "Prioritize", "Evidence, warmth, timing, and a clear next action"),
    ("03", "Connect", "Warm introductions and reviewed, permission-based outreach"),
    ("04", "Prepare", "Meeting context, objectives, and questions"),
    ("05", "Execute", "Activity logging, meetings, and timely follow-through"),
    ("06", "Coordinate", "Documented needs and approved specialist workflows"),
    ("07", "Expand", "Reviews, introductions, and community participation"),
    ("08", "Learn", "Use actual conversion data to improve the plan"),
]
for i, (num, title, desc) in enumerate(modules):
    with cols[i % 4]:
        st.markdown(
            f"<div class='brand-hero' style='padding:1rem 1.05rem;min-height:145px;margin-bottom:.8rem'>"
            f"<div class='brand-kicker'>{num}</div><div class='brand-hero-title' style='font-size:1.08rem'>{title}</div>"
            f"<div class='brand-hero-copy' style='font-size:.86rem'>{desc}</div></div>",
            unsafe_allow_html=True,
        )

st.subheader("Command Center Modules")
t1, t2, t3 = st.tabs(["Acquire", "Develop", "Execute"])
with t1:
    a, b, c = st.columns(3)
    a.markdown("**Prospect Discovery**\n\nBrowse curated business, household/COI, career-transition, and referral research.")
    b.markdown("**Opportunity Radar**\n\nReview public timing signals as hypotheses that require human verification.")
    c.markdown("**Lead Lists**\n\nReview source-aware working lists and export only after validation.")
with t2:
    a, b, c = st.columns(3)
    a.markdown("**Influencer & Referral Network**\n\nDevelop relationship opportunities based on local audience overlap.")
    b.markdown("**Event Prospecting**\n\nTrack verified events, introductions, follow-ups, and appointments.")
    c.markdown("**Practice Strategy**\n\nKeep market focus and business-development choices visible.")
with t3:
    a, b, c = st.columns(3)
    a.markdown("**Daily War Room**\n\nReverse-engineer a goal into production and activity requirements.")
    b.markdown("**Meeting Intelligence**\n\nPrepare with public context and a clear meeting objective.")
    c.markdown("**401(k) Rollover Playbook**\n\nUse a balanced alternatives review and follow current firm procedures.")

st.divider()
st.caption(
    f"Chris Haake Command Center • {today.isoformat()} • Central Florida • "
    "Personal productivity and research aid; not a client system of record or a substitute for NYL approval."
)
