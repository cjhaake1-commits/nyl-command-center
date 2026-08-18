from __future__ import annotations

from datetime import date

import streamlit as st

from core.branding import brand_hero
from data.hnw_leads import HNW_LEADS
from data.marketing_network_leads import MARKETING_NETWORK_LEADS
from data.public_leads import PUBLIC_LEADS

st.set_page_config(page_title="Command Center | Chris Haake", page_icon="◆", layout="wide")

brand_hero(
    "Growth Command Center",
    "Your operating cockpit for Central Florida prospect discovery, relationship development, marketing reach, pipeline execution and production discipline.",
    "Chris Haake • Advisor Growth OS",
)

business_count = len(PUBLIC_LEADS)
hnw_count = len(HNW_LEADS)
network_count = len(MARKETING_NETWORK_LEADS)
total_discovery = business_count + hnw_count + network_count
high_fit_network = sum(1 for x in MARKETING_NETWORK_LEADS if float(x.get("Audience fit score", 0) or 0) >= 95)
high_hnw = sum(1 for x in HNW_LEADS if float(x.get("Opportunity score", 0) or 0) >= 95)

s1, s2, s3 = st.columns([1, 1, 2])
s1.success("SYSTEM • ONLINE")
s2.info("DISCOVERY ENGINE • ACTIVE")
s3.caption("Public-source intelligence is kept traceable. Regulated recommendations, communications and advertising remain inside approved processes.")

st.subheader("Executive Snapshot")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Discovery Universe", total_discovery, "live records")
c2.metric("Business Prospects", business_count)
c3.metric("HNW / COI", hnw_count, f"{high_hnw} priority")
c4.metric("Referral Network", network_count, f"{high_fit_network} fit 95+")
c5.metric("Daily Priority", "20", "relationship actions")

st.subheader("Today's Operating Priorities")
left, center, right = st.columns([1.15, 1, 1])
with left:
    st.markdown("### 01 • Build Pipeline")
    st.write("Work the highest-scoring business and household prospects first. Prioritize fresh triggers and credible warm paths over generic cold volume.")
    st.progress(0.72, text="Discovery engine coverage")
    st.caption("Hourly research feeds Business, HNW/COI and Marketing/Referral discovery lanes.")
with center:
    st.markdown("### 02 • Build Relationships")
    st.write("Develop COIs, influencers, Realtors, attorneys, CPAs, bankers and community connectors who can compound access to the right households.")
    st.progress(0.58, text="Network development")
    st.caption("Audience fit and relationship leverage matter more than raw follower count.")
with right:
    st.markdown("### 03 • Execute")
    st.write("Move research into dated next actions: introductions, calls, coffees, events, meeting preparation and disciplined follow-through.")
    st.progress(0.45, text="Execution rhythm")
    st.caption("Use Daily War Room for production math and activity tracking.")

st.subheader("Growth Flywheel")
cols = st.columns(4)
modules = [
    ("01", "Discover", "Public signals, referrals, events, creators and business triggers"),
    ("02", "Prioritize", "Opportunity, warmth, timing, audience fit and strategic value"),
    ("03", "Connect", "Warm paths, COIs, LinkedIn, events and relationship-first outreach"),
    ("04", "Prepare", "Research, first-touch context and meeting intelligence"),
    ("05", "Execute", "Touches, meetings, diagnostics and dated next actions"),
    ("06", "Coordinate", "Documented needs and approved specialist workflows"),
    ("07", "Expand", "Reviews, introductions, community and additional relationships"),
    ("08", "Learn", "Conversion data continuously improves prioritization"),
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
    a.markdown("**Prospect Discovery**\n\nBusiness owners, HNW households, COIs and public growth triggers.")
    b.markdown("**Opportunity Radar**\n\nSurface timing signals and research-backed hypotheses without assuming private needs.")
    c.markdown("**Lead Lists**\n\nTurn research into controlled, source-aware working lists and exports.")
with t2:
    a, b, c = st.columns(3)
    a.markdown("**Influencer Network**\n\nReal-estate, home, design and lifestyle relationships ranked by audience fit.")
    b.markdown("**LinkedIn Network**\n\nVerify professional identity, mutual context and warm paths before connecting.")
    c.markdown("**Marketing Command Center**\n\nPlan compliant local visibility, events, content and relationship campaigns.")
with t3:
    a, b, c = st.columns(3)
    a.markdown("**Daily War Room**\n\nReverse-engineer goals into today's exact activity mission.")
    b.markdown("**Meeting Intelligence**\n\nPrepare for higher-quality conversations with public context and clear objectives.")
    c.markdown("**Sales Autopilot**\n\nKeep follow-up, stale opportunities and execution discipline visible.")

st.divider()
st.caption(f"Chris Haake Command Center • {date.today().isoformat()} • Central Florida Growth OS • Research signals are not financial recommendations.")
