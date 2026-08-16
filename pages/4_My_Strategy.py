from __future__ import annotations

import pandas as pd
import streamlit as st

from core.personalized_strategy import (
    COI_ECOSYSTEMS,
    PERSONALIZED_MESSAGE_PILLARS,
    PERSONALIZED_POSITIONING,
    PRIORITY_NICHES,
    RELATIONSHIP_EXPANSION_SEQUENCE,
)

st.set_page_config(page_title="My NYL Strategy", page_icon="💎", layout="wide")

st.title("My NYL Strategy")
st.caption("A relationship-first growth strategy tailored to your luxury/high-value sales background and Greater Orlando market.")

st.success(PERSONALIZED_POSITIONING["headline"])
st.write(PERSONALIZED_POSITIONING["why_it_fits"])
st.info(PERSONALIZED_POSITIONING["operating_rule"])

st.subheader("Priority Niches")
st.dataframe(pd.DataFrame(PRIORITY_NICHES), width="stretch", hide_index=True)

st.subheader("COI Ecosystems to Build")
st.dataframe(pd.DataFrame(COI_ECOSYSTEMS), width="stretch", hide_index=True)

st.subheader("Relationship Expansion Sequence")
st.dataframe(pd.DataFrame(RELATIONSHIP_EXPANSION_SEQUENCE), width="stretch", hide_index=True)

st.subheader("Positioning Pillars")
for pillar in PERSONALIZED_MESSAGE_PILLARS:
    st.markdown(f"- {pillar}")

st.warning(
    "Use this strategy as positioning and workflow guidance. Any insurance/securities recommendation, advertising, solicitation, client review, or product discussion must follow your licensing, NYL compliance, suitability, privacy, and approved-system requirements."
)
