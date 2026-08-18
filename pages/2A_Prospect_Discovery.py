from __future__ import annotations

import pandas as pd
import streamlit as st

from data.public_leads import PUBLIC_LEADS
from data.hnw_leads import HNW_LEADS
from data.marketing_network_leads import MARKETING_NETWORK_LEADS

st.set_page_config(page_title="NYL Prospect Discovery", page_icon="🎯", layout="wide")

st.title("Prospect Discovery")
st.caption(
    "Verified public-source discovery lanes for Central Florida business prospects, HNW/household and COI relationships, "
    "and marketing/referral-network opportunities. Public signals are research hypotheses, not assumptions about private financial needs."
)

business_df = pd.DataFrame(PUBLIC_LEADS)
hnw_df = pd.DataFrame(HNW_LEADS)
marketing_df = pd.DataFrame(MARKETING_NETWORK_LEADS)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Business / public leads", len(business_df))
c2.metric("HNW / household + COI", len(hnw_df))
c3.metric("Marketing / referral", len(marketing_df))
c4.metric("Total discovery records", len(business_df) + len(hnw_df) + len(marketing_df))

st.info(
    "Research standard: use lawful public sources, keep observable facts separate from hypotheses, verify time-sensitive signals, "
    "and use warm introductions whenever possible. Any financial-services advertising, testimonials, influencer compensation, "
    "or referral arrangement must follow NYL/carrier compliance before execution."
)

tab_business, tab_hnw, tab_marketing = st.tabs([
    "Business Prospects",
    "HNW / Households & COIs",
    "Marketing / Referral Network",
])

with tab_business:
    st.subheader("Business Prospects")
    st.caption("Founder-led companies, growth triggers, public registrations, chamber relationships and other public business signals.")
    if business_df.empty:
        st.info("No business prospects loaded yet.")
    else:
        q = st.text_input("Search business leads", key="business_search")
        view = business_df.copy()
        if q.strip():
            mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
            view = view[mask]
        sort_col = "Opportunity score" if "Opportunity score" in view.columns else view.columns[0]
        if sort_col in view.columns:
            view = view.sort_values(sort_col, ascending=False, kind="stable")
        preferred = [
            "Lead type", "Name", "Company", "Role", "Industry", "Area", "Opportunity score", "Warmth score",
            "Trigger", "Warm path", "Why now", "Next action", "Verified date", "Status", "Source URL"
        ]
        cols = [c for c in preferred if c in view.columns]
        st.dataframe(view[cols], width="stretch", hide_index=True)

with tab_hnw:
    st.subheader("HNW / Households & Centers of Influence")
    st.caption(
        "Households and relationship multipliers identified from documented founder ownership, philanthropy, family-enterprise, "
        "investment, real-estate or professional-advisor signals. Net worth is not inferred when it is not credibly published."
    )
    if hnw_df.empty:
        st.info("No HNW/COI records loaded yet.")
    else:
        h1, h2 = st.columns(2)
        q = h1.text_input("Search HNW / COI records", key="hnw_search")
        lead_types = sorted(str(x) for x in hnw_df.get("Lead type", pd.Series(dtype=str)).dropna().unique())
        selected_types = h2.multiselect("Lead type", lead_types, default=lead_types)
        view = hnw_df.copy()
        if selected_types and "Lead type" in view.columns:
            view = view[view["Lead type"].astype(str).isin(selected_types)]
        if q.strip():
            mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
            view = view[mask]
        if "Opportunity score" in view.columns:
            view = view.sort_values(["Opportunity score", "Warmth score"], ascending=[False, False], kind="stable")
        preferred = [
            "Lead type", "Name", "Company", "Role", "Area", "Signal", "Signal strength", "Opportunity score", "Warmth score",
            "Warm path", "Why now", "Next action", "Verified date", "Status", "Source URL"
        ]
        cols = [c for c in preferred if c in view.columns]
        st.dataframe(view[cols], width="stretch", hide_index=True)

with tab_marketing:
    st.subheader("Marketing / Referral Network")
    st.caption(
        "Central Florida real-estate, home, design, lifestyle and community creators ranked by audience fit, reach and referral potential. "
        "Follower counts are time-stamped public estimates and should be refreshed before campaign decisions."
    )
    if marketing_df.empty:
        st.info("No marketing/referral records loaded yet.")
    else:
        m1, m2 = st.columns(2)
        q = m1.text_input("Search marketing / referral leads", key="marketing_search")
        categories = sorted(str(x) for x in marketing_df.get("Category", pd.Series(dtype=str)).dropna().unique())
        selected_categories = m2.multiselect("Category", categories, default=categories)
        view = marketing_df.copy()
        if selected_categories and "Category" in view.columns:
            view = view[view["Category"].astype(str).isin(selected_categories)]
        if q.strip():
            mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
            view = view[mask]
        if "Audience fit score" in view.columns:
            view = view.sort_values(["Audience fit score", "Reach score"], ascending=[False, False], kind="stable")
        preferred = [
            "Name", "Brand", "Category", "Area", "Audience size", "Audience fit score", "Reach score", "Referral potential",
            "Why fit", "Best angle", "Verified date", "Status", "Source URL"
        ]
        cols = [c for c in preferred if c in view.columns]
        st.dataframe(view[cols], width="stretch", hide_index=True)

st.divider()
st.caption(
    "These discovery records are research inputs. Before outreach, confirm public-source accuracy, applicable consent / do-not-contact rules, "
    "platform terms and NYL-approved communications processes."
)
