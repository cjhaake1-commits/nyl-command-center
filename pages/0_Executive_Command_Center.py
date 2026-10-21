from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from data.hnw_leads import HNW_LEADS
from data.marketing_network_leads import MARKETING_NETWORK_LEADS
from data.public_leads import PUBLIC_LEADS

st.set_page_config(page_title="Command Center | Chris Haake", page_icon="◆", layout="wide")

brand_hero(
    "Growth Command Center",
    "A practical operating cockpit for building a focused Central Florida practice: discover, verify, connect, prepare, follow through, and improve.",
    "Chris Haake • Advisor Growth OS",
)

business_count = len(PUBLIC_LEADS)
hnw_count = len(HNW_LEADS)
network_count = len(MARKETING_NETWORK_LEADS)
total_discovery = business_count + hnw_count + network_count
high_fit_network = sum(1 for x in MARKETING_NETWORK_LEADS if float(x.get("Audience fit score", 0) or 0) >= 95)
high_hnw = sum(1 for x in HNW_LEADS if float(x.get("Opportunity score", 0) or 0) >= 95)

s1, s2, s3 = st.columns([1, 1, 2])
s1.info("DEMO WORKSPACE • ONLINE")
s2.info("CURATED SEED DATA • LOADED")
s3.caption(
    "This workspace is a planning prototype, not connected to NYL production systems. "
    "Verify current sources and use firm-approved systems and processes for prospect records, communications, and recommendations."
)

st.subheader("Executive Snapshot")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Research Records", total_discovery, "curated seed files")
c2.metric("Business Prospects", business_count)
c3.metric("HNW / COI", hnw_count, f"{high_hnw} high-score research records")
c4.metric("Referral Network", network_count, f"{high_fit_network} high-fit research records")
c5.metric("Daily Relationship Actions", "20", "planning target")

st.subheader("Growth Priorities")
st.caption(
    "Targets describe the intended operating plan; this prototype does not claim they are completed or synced to Salesforce."
)
goals = [
    {
        "Goal": "Build a qualified prospect universe",
        "Target": "5,000 validated net-new prospects",
        "Proof": "Count only accepted Salesforce Created rows; deduplicate against existing records and retain source evidence.",
        "Next action": "Verify identity, business fit, public source, and contact details before approved import or outreach.",
    },
    {
        "Goal": "Earn the opportunity and ramp well",
        "Target": "First 100 qualified accounts, then a consistent weekly rhythm",
        "Proof": "Manager-confirmed onboarding, approved tools, dated next actions, and weekly activity/conversion review.",
        "Next action": "Ask the office which measures and systems define a successful first 30, 60, and 90 days.",
    },
    {
        "Goal": "Create a repeatable practice",
        "Target": "A focused Central Florida acquisition and relationship plan",
        "Proof": "Track conversations, held meetings, next steps, introductions, and conversion by source.",
        "Next action": "Test a small number of owner, professional, COI, and event lanes; invest more time in what converts.",
    },
]
st.dataframe(pd.DataFrame(goals), width="stretch", hide_index=True)

st.subheader("Today's Operating Priorities")
left, center, right = st.columns([1.15, 1, 1])
with left:
    st.markdown("### 01 • Verify & Prioritize")
    st.write("Start with a credible public signal, a verified identity, and a relevant reason to connect. Treat fit scores as research aids, not evidence of a person's needs.")
    st.caption("Today: select a small, reviewable set of qualified accounts and confirm each source.")
with center:
    st.markdown("### 02 • Build Relationships")
    st.write("Develop COI and community relationships through useful professional conversations. Earn trust before asking for introductions.")
    st.caption("Today: choose a few meaningful relationship actions and record the next step.")
with right:
    st.markdown("### 03 • Learn & Improve")
    st.write("Review activity and conversion by source. Adjust the plan from observed results instead of relying on fixed assumptions.")
    st.caption("Today: use Daily War Room for editable goal math and activity tracking.")

st.subheader("Growth Flywheel")
cols = st.columns(4)
modules = [
    ("01", "Discover", "Public signals, referrals, events, and business triggers"),
    ("02", "Prioritize", "Fit, warmth, timing, and a credible reason to connect"),
    ("03", "Connect", "Warm paths, COIs, LinkedIn, and community relationships"),
    ("04", "Prepare", "Public context, meeting goals, and thoughtful questions"),
    ("05", "Execute", "Follow-up, meetings, dated next actions, and review"),
    ("06", "Coordinate", "Documented needs and approved specialist workflows"),
    ("07", "Expand", "Service, reviews, introductions, and community"),
    ("08", "Learn", "Conversion data improves where time is invested"),
]
for i, (num, title, desc) in enumerate(modules):
    with cols[i % 4]:
        st.markdown(
            f"<div class='brand-hero' style='padding:1rem 1.05rem;min-height:145px;margin-bottom:.8rem'>"
            f"<div class='brand-kicker'>{num}</div><div class='brand-hero-title' style='font-size:1.08rem'>{title}</div>"
            f"<div class='brand-hero-copy' style='font-size:.86rem'>{desc}</div></div>",
            unsafe_allow_html=True,
        )

st.subheader("Intelligence Stack")
t1, t2, t3 = st.tabs(["Acquire", "Develop", "Execute"])
with t1:
    a, b, c = st.columns(3)
    a.markdown("**Prospect Discovery**\n\nBusiness owners, households, COIs, and public growth signals.")
    b.markdown("**Opportunity Radar**\n\nResearch timing signals as hypotheses; confirm context in conversation.")
    c.markdown("**Lead Lists**\n\nReview source-aware records and deduplication before any approved workflow.")
with t2:
    a, b, c = st.columns(3)
    a.markdown("**Influencer Network**\n\nEvaluate professional and community relationships by relevance.")
    b.markdown("**LinkedIn Network**\n\nCheck professional identity, mutual context, and warm paths.")
    c.markdown("**Marketing Command Center**\n\nPlan local visibility, events, and content for review through applicable firm processes.")
with t3:
    a, b, c = st.columns(3)
    a.markdown("**Daily War Room**\n\nTranslate an editable goal into activity assumptions.")
    b.markdown("**Meeting Intelligence**\n\nPrepare for conversations and structure follow-up.")
    c.markdown("**Sales Autopilot**\n\nReview due follow-up, stale opportunities, and execution discipline.")

st.divider()
st.caption(
    f"Chris Haake Command Center • {datetime.now(ZoneInfo('America/New_York')).date().isoformat()} • "
    "Central Florida planning prototype • Research signals are not recommendations or proof of need."
)
