from __future__ import annotations

from datetime import date

import streamlit as st

from core.branding import brand_hero
from core.rep_profile import REP_NAME, TERRITORY_LABEL, TERRITORY_GROWTH_LABEL
from data.paul_market import HNW_LEADS, MARKETING_NETWORK_LEADS, PUBLIC_LEADS

st.set_page_config(page_title=f"Command Center | {REP_NAME}", page_icon="◆", layout="wide")

brand_hero(
    "Growth Command Center",
    f"Your operating cockpit for {TERRITORY_LABEL} prospect discovery, relationship development, marketing reach, pipeline execution and production discipline.",
    f"{REP_NAME} • Advisor Growth OS",
)

business_count = len(PUBLIC_LEADS)
hnw_count = len(HNW_LEADS)
network_count = len(MARKETING_NETWORK_LEADS)
total_discovery = business_count + hnw_count + network_count

s1, s2, s3 = st.columns([1, 1, 2])
s1.success("SYSTEM • ONLINE")
s2.info("DISCOVERY ENGINE • ACTIVE")
s3.caption("Paul's tenant is isolated from the Chris Haake / Central Florida prospect universe.")

st.subheader("Executive Snapshot")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Discovery Universe", total_discovery, "Paul-only records")
c2.metric("Business Prospects", business_count)
c3.metric("HNW / COI", hnw_count)
c4.metric("Referral Network", network_count)
c5.metric("Territory", "20 mi", "93065 center")

if total_discovery == 0:
    st.info("Paul's California prospect universe is clean and ready for verified Simi Valley-area lead loading. No Chris/Florida records are included.")

st.subheader("Today's Operating Priorities")
left, center, right = st.columns(3)
with left:
    st.markdown("### 01 • Build Pipeline")
    st.write("Prioritize verified business owners, professionals and households inside the configured territory, using public evidence and credible relationship paths.")
with center:
    st.markdown("### 02 • Build Relationships")
    st.write("Develop local COIs, attorneys, CPAs, bankers, Realtors, business groups and community connectors.")
with right:
    st.markdown("### 03 • Execute")
    st.write("Move approved research into dated next actions and use the Salesforce-ready and Personalized Scripts tabs for prepared lead packages.")

st.subheader("Growth Flywheel")
modules = [
    ("Discover", "Public signals and local business/professional triggers"),
    ("Prioritize", "Opportunity, timing, accessibility and relationship value"),
    ("Prepare", "Verified contact routes, rationale and personalized scripts"),
    ("Review", "Compliance and product-authority gates remain separate"),
]
cols = st.columns(4)
for col, (title, copy) in zip(cols, modules):
    with col:
        st.markdown(f"**{title}**")
        st.caption(copy)

st.divider()
st.caption(f"{REP_NAME} Command Center • {date.today().isoformat()} • {TERRITORY_GROWTH_LABEL} • Research signals are not financial recommendations.")
