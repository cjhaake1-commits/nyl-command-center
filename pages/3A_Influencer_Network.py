from __future__ import annotations

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from core.rep_profile import REP_NAME, TERRITORY_LABEL
from data.paul_market import MARKETING_NETWORK_LEADS

st.set_page_config(page_title=f"Influencer Network | {REP_NAME}", page_icon="📱", layout="wide")
brand_hero(
    "Influencer & Referral Network",
    f"Build relationships with local creators and community connectors relevant to {TERRITORY_LABEL}.",
    f"{REP_NAME} • Marketing & Network",
)
st.warning("Paid promotion, testimonials, endorsements, influencer compensation or referral arrangements involving financial services require applicable approval before execution.")

df = pd.DataFrame(MARKETING_NETWORK_LEADS)
if df.empty:
    st.info("No Paul-specific referral-network candidates are loaded yet. Chris Haake's Central Florida network is not used in this tenant.")
else:
    st.dataframe(df, width="stretch", hide_index=True)

st.subheader("How to Use This Network")
a, b, c = st.columns(3)
with a:
    st.markdown("**Relationship First**")
    st.write("Meet through legitimate local events, mutual business relationships and community circles before proposing campaigns.")
with b:
    st.markdown("**Audience Before Followers**")
    st.write("Prioritize local relevance and relationship potential over raw follower count.")
with c:
    st.markdown("**Collaborate Carefully**")
    st.write("Keep compensated or promotional activity inside approved compliance processes.")
