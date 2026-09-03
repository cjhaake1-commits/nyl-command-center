from __future__ import annotations

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from core.rep_profile import REP_NAME, TERRITORY_LABEL
from data.paul_market import PUBLIC_LEADS, HNW_LEADS, MARKETING_NETWORK_LEADS

st.set_page_config(page_title=f"Prospect Discovery | {REP_NAME}", page_icon="🎯", layout="wide")
brand_hero(
    "Prospect Discovery",
    f"A continuously growing public-source intelligence layer for {TERRITORY_LABEL}: business triggers, professionals, COIs and referral networks.",
    f"{REP_NAME} • Intelligence Engine",
)

business_df = pd.DataFrame(PUBLIC_LEADS)
hnw_df = pd.DataFrame(HNW_LEADS)
marketing_df = pd.DataFrame(MARKETING_NETWORK_LEADS)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Business Leads", len(business_df))
c2.metric("HNW / COI", len(hnw_df))
c3.metric("Referral Network", len(marketing_df))
c4.metric("Total Intelligence", len(business_df) + len(hnw_df) + len(marketing_df))

st.info("Paul's discovery data is tenant-isolated. Public facts and planning hypotheses stay separate; outreach remains subject to authorization and compliance review.")

t1, t2, t3 = st.tabs(["Business Prospects", "Individuals / COIs", "Referral Network"])
with t1:
    if business_df.empty:
        st.info("No verified Simi Valley-area business prospects loaded yet.")
    else:
        st.dataframe(business_df, width="stretch", hide_index=True)
with t2:
    if hnw_df.empty:
        st.info("No verified individual / COI prospects loaded yet.")
    else:
        st.dataframe(hnw_df, width="stretch", hide_index=True)
with t3:
    if marketing_df.empty:
        st.info("No verified local referral-network candidates loaded yet.")
    else:
        st.dataframe(marketing_df, width="stretch", hide_index=True)

st.divider()
st.caption("Research inputs only. Confirm source accuracy, contact eligibility, licensing, privacy, suppression and NYL communications requirements before outreach.")
