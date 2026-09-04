from __future__ import annotations

from datetime import date

import streamlit as st

from core.branding import apply_brand_theme, brand_hero
from core.rep_profile import REP_NAME, TERRITORY_LABEL, TERRITORY_GROWTH_LABEL
from data.paul_market import HNW_LEADS, MARKETING_NETWORK_LEADS, PUBLIC_LEADS

st.set_page_config(page_title=f"Command Center | {REP_NAME}", page_icon="📈", layout="wide")
apply_brand_theme()

st.markdown(
    f"""
    <div style="margin-bottom:.75rem;padding:.65rem .9rem;border-left:3px solid #D7A449;background:rgba(215,164,73,.05);border-radius:0 10px 10px 0;">
      <div style="color:#F0C36A;font-size:.72rem;letter-spacing:.16em;font-weight:800;">NEW YORK LIFE • {TERRITORY_GROWTH_LABEL}</div>
      <div style="color:white;font-size:1.05rem;font-weight:700;margin-top:.15rem;">{REP_NAME} Advisor Command Center</div>
    </div>
    """,
    unsafe_allow_html=True,
)

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
for column, number, title, copy in [
    (left, "01", "Build Pipeline", "Prioritize verified business owners, professionals and households inside the configured territory, using public evidence and credible relationship paths."),
    (center, "02", "Build Relationships", "Develop local COIs, attorneys, CPAs, bankers, Realtors, business groups and community connectors."),
    (right, "03", "Execute", "Move approved research into dated next actions and use the Salesforce-ready and Personalized Scripts tabs for prepared lead packages."),
]:
    with column:
        st.markdown(
            f"<div class='brand-hero' style='min-height:170px;padding:1rem 1.1rem'>"
            f"<div class='brand-kicker'>{number}</div>"
            f"<div class='brand-hero-title' style='font-size:1.15rem'>{title}</div>"
            f"<div class='brand-hero-copy' style='font-size:.88rem'>{copy}</div></div>",
            unsafe_allow_html=True,
        )

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
        st.markdown(
            f"<div class='brand-hero' style='min-height:135px;padding:1rem'>"
            f"<div class='brand-hero-title' style='font-size:1rem'>{title}</div>"
            f"<div class='brand-hero-copy' style='font-size:.82rem'>{copy}</div></div>",
            unsafe_allow_html=True,
        )

st.subheader("Command Stack")
t1, t2, t3 = st.tabs(["Acquire", "Develop", "Execute"])
with t1:
    a, b, c = st.columns(3)
    a.markdown("**Prospect Discovery**\n\nBusiness owners, professionals, households and public growth triggers.")
    b.markdown("**Opportunity Radar**\n\nSurface timing signals and research-backed hypotheses.")
    c.markdown("**Salesforce Ready Import**\n\nNet-new verified contacts in the approved import structure.")
with t2:
    a, b, c = st.columns(3)
    a.markdown("**Referral Network**\n\nDevelop local COIs and high-value relationship paths.")
    b.markdown("**LinkedIn Network**\n\nVerify professional identity and mutual context.")
    c.markdown("**Marketing Command Center**\n\nPlan compliant local visibility and relationship campaigns.")
with t3:
    a, b, c = st.columns(3)
    a.markdown("**Daily War Room**\n\nReverse-engineer goals into today's exact activity mission.")
    b.markdown("**Personalized Scripts**\n\nRelationship-first call and email language for each lead.")
    c.markdown("**Make a Request**\n\nTailor products, territory, lead focus and workflows as Paul advances.")

st.divider()
st.caption(f"{REP_NAME} Command Center • {date.today().isoformat()} • {TERRITORY_GROWTH_LABEL} • Research signals are not financial recommendations.")
