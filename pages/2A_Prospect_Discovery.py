from __future__ import annotations

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from data.public_leads import PUBLIC_LEADS
from data.hnw_leads import HNW_LEADS
from data.marketing_network_leads import MARKETING_NETWORK_LEADS
from data.rollover_leads import ROLLOVER_LEADS, ROLLOVER_SCREEN, ROLLOVER_REVIEW_POINTS, ROLLOVER_OUTREACH

st.set_page_config(page_title="Prospect Discovery | Chris Haake", page_icon="🎯", layout="wide")

brand_hero(
    "Prospect Discovery",
    "A continuously growing Central Florida intelligence layer: business triggers, HNW and household signals, centers of influence, career transitions, and high-fit referral networks — all tied back to public evidence.",
    "Chris Haake • Intelligence Engine",
)

business_df = pd.DataFrame(PUBLIC_LEADS)
hnw_df = pd.DataFrame(HNW_LEADS)
marketing_df = pd.DataFrame(MARKETING_NETWORK_LEADS)
rollover_df = pd.DataFrame(ROLLOVER_LEADS)

def num_high(df: pd.DataFrame, col: str, threshold: float) -> int:
    if df.empty or col not in df.columns:
        return 0
    return int((pd.to_numeric(df[col], errors="coerce") >= threshold).sum())

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Business Leads", len(business_df), f"{num_high(business_df, 'Opportunity score', 90)} score 90+")
c2.metric("HNW / COI", len(hnw_df), f"{num_high(hnw_df, 'Opportunity score', 95)} score 95+")
c3.metric("Rollover Signals", len(rollover_df), "former-employer career transitions")
c4.metric("Referral Network", len(marketing_df), f"{num_high(marketing_df, 'Audience fit score', 95)} fit 95+")
c5.metric("Research Cadence", "Hourly", "verified batches")

st.info("Evidence standard: public-source facts stay separate from planning hypotheses. Prefer warm introductions. Never infer private financial condition, retirement-plan participation, account balance, or rollover need from career or social-media signals.")

tab_business, tab_hnw, tab_rollover, tab_marketing = st.tabs(["Business Prospects", "HNW / Households & COIs", "401(k) / Former Employer", "Marketing / Referral Network"])

with tab_business:
    top_left, top_right = st.columns([1.5, 1])
    with top_left:
        st.markdown("### Business Intelligence")
        st.caption("Founder-led companies, registrations, expansions, hiring, contracts, chambers and other observable business triggers.")
    with top_right:
        q = st.text_input("Search business intelligence", key="business_search", placeholder="Name, company, industry, area, trigger...")
    view = business_df.copy()
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if not view.empty and "Opportunity score" in view.columns:
        view = view.sort_values(["Opportunity score", "Warmth score"], ascending=[False, False], kind="stable")
    if view.empty:
        st.info("No business prospects match this view.")
    else:
        st.markdown("#### Priority Queue")
        for _, row in view.head(5).iterrows():
            with st.expander(f"{row.get('Name','')} • {row.get('Company','')} | Opportunity {row.get('Opportunity score','—')}"):
                a, b = st.columns([1.2, 1])
                a.write(f"**Why now:** {row.get('Why now','')}")
                a.write(f"**Trigger:** {row.get('Trigger','')}")
                b.write(f"**Warm path:** {row.get('Warm path','')}")
                b.write(f"**Next action:** {row.get('Next action','')}")
                if row.get("Source URL"):
                    st.caption(f"Source: {row.get('Source URL')}")
        preferred = ["Name", "Company", "Role", "Industry", "Area", "Opportunity score", "Warmth score", "Trigger", "Warm path", "Next action", "Verified date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

with tab_hnw:
    head, controls = st.columns([1.35, 1])
    with head:
        st.markdown("### Household & Influence Intelligence")
        st.caption("Documented founder ownership, philanthropy, family enterprise, investment activity and trusted-advisor relationships.")
    with controls:
        q = st.text_input("Search households / COIs", key="hnw_search", placeholder="Name, organization, area, signal...")
    lead_types = sorted(str(x) for x in hnw_df.get("Lead type", pd.Series(dtype=str)).dropna().unique())
    selected_types = st.multiselect("Relationship lane", lead_types, default=lead_types, key="hnw_types")
    view = hnw_df.copy()
    if selected_types and "Lead type" in view.columns:
        view = view[view["Lead type"].astype(str).isin(selected_types)]
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if not view.empty and "Opportunity score" in view.columns:
        view = view.sort_values(["Opportunity score", "Warmth score"], ascending=[False, False], kind="stable")
    if view.empty:
        st.info("No HNW / COI records match this view.")
    else:
        st.markdown("#### Highest-Leverage Relationships")
        cards = st.columns(3)
        for i, (_, row) in enumerate(view.head(3).iterrows()):
            with cards[i]:
                st.metric(str(row.get("Name", "Prospect")), f"{row.get('Opportunity score','—')}/100", str(row.get("Lead type", "")))
                st.caption(str(row.get("Signal", "")))
        preferred = ["Lead type", "Name", "Company", "Role", "Area", "Signal", "Signal strength", "Opportunity score", "Warmth score", "Warm path", "Next action", "Verified date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

with tab_rollover:
    st.markdown("### Former-Employer Retirement Plan Signals")
    st.caption("Find public career transitions where a person left an employer with 100+ employees after 3+ years. This is a reason to offer a retirement-plan review, not evidence that a 401(k) exists or that a rollover is appropriate.")

    r1, r2, r3, r4 = st.columns(4)
    r1.metric("Former employer size", f"{ROLLOVER_SCREEN['former_employer_min_headcount']}+")
    r2.metric("Minimum tenure", f"{ROLLOVER_SCREEN['former_employer_min_tenure_years']:.0f}+ years")
    r3.metric("Preferred recency", f"{ROLLOVER_SCREEN['preferred_change_recency_months']} months")
    r4.metric("Geography", "Central Florida")

    st.warning("Do not say or imply that leaving an old employer plan is a mistake. A participant may reasonably keep assets in the old plan, move them to a new employer plan if permitted, roll to an IRA, or take a distribution. Any recommendation must compare the actual alternatives, costs, investments, services, tax effects and protections.")

    q = st.text_input("Search rollover signals", key="rollover_search", placeholder="Name, former employer, new employer, title, area...")
    view = rollover_df.copy()
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if view.empty:
        st.info("No verified rollover-signal leads have been added yet. Research uses public LinkedIn/Facebook professional information, company bios and career announcements; private social content is excluded.")
    else:
        preferred = ["Name", "Current Company", "Current Role", "Former Employer", "Former Role", "Former Employer Size", "Tenure Years", "Change Date", "Area", "Public Contact", "Signal", "Source URL", "Verified Date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

    st.markdown("#### Dossier review points")
    for item in ROLLOVER_REVIEW_POINTS:
        st.write(f"- {item}")

    st.markdown("#### Meeting-first outreach")
    st.text_area("Phone", ROLLOVER_OUTREACH["phone"], height=190, key="rollover_phone")
    st.text_area("Email", ROLLOVER_OUTREACH["email"], height=280, key="rollover_email")

with tab_marketing:
    head, controls = st.columns([1.35, 1])
    with head:
        st.markdown("### Referral Audience Intelligence")
        st.caption("Creators and community accounts selected for Central Florida homeowner, mover, investor, affluent-family and business-owner audience overlap.")
    with controls:
        q = st.text_input("Search referral network", key="marketing_search", placeholder="Creator, handle, category, market...")
    view = marketing_df.copy()
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if not view.empty and "Audience fit score" in view.columns:
        view = view.sort_values(["Audience fit score", "Reach score"], ascending=[False, False], kind="stable")
    if view.empty:
        st.info("No marketing/referral records match this view.")
    else:
        st.markdown("#### Top Audience Matches")
        cards = st.columns(3)
        for i, (_, row) in enumerate(view.head(3).iterrows()):
            with cards[i]:
                st.metric(str(row.get("Name", "Creator")), f"{row.get('Audience fit score','—')}/100", str(row.get("Audience size", "")))
                st.caption(str(row.get("Why fit", "")))
        preferred = ["Name", "Brand", "Category", "Area", "Audience size", "Audience fit score", "Reach score", "Referral potential", "Why fit", "Best angle", "Verified date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

st.divider()
st.caption("Research inputs only. Confirm source accuracy and applicable consent, privacy, do-not-contact, platform, licensing, fiduciary/rollover and NYL communications requirements before outreach or campaign execution.")
