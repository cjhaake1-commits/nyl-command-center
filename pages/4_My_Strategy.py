from __future__ import annotations

import pandas as pd
import streamlit as st

from core.rep_profile import REP_NAME, TERRITORY_LABEL

st.set_page_config(page_title=f"Practice Strategy | {REP_NAME}", page_icon="💎", layout="wide")
st.title("Practice Strategy")
st.caption(f"Relationship-first growth framework for {REP_NAME} in {TERRITORY_LABEL}.")

st.success("Build a local relationship network first, then let verified authority and approved discovery determine which planning conversations are appropriate.")
st.info("Paul may have broader product access than the base clone. Use Make a Request to add verified products, registrations, target segments or approved messaging rather than assuming authority.")

st.subheader("Initial Priority Lanes")
st.dataframe(pd.DataFrame([
    ["Business owners / founders", "Key-person, continuity, succession and benefits discovery when authorized"],
    ["Professional practices", "Owner dependency, disability/overhead, continuity and broader planning"],
    ["Executives / professionals", "Protection, retirement and broader planning as authorized"],
    ["Centers of influence", "CPAs, attorneys, bankers, Realtors, business advisers and community connectors"],
    ["Growing employers", "Executive/employee benefits relevance where authorized and appropriate"],
], columns=["Lane", "Why it matters"]), width="stretch", hide_index=True)

st.subheader("Operating Sequence")
st.dataframe(pd.DataFrame([
    [1, "Discover", "Find public, relevant local signals"],
    [2, "Verify", "Confirm identity, source, territory and public contact route"],
    [3, "Prioritize", "Score opportunity separately from contact eligibility"],
    [4, "Prepare", "Create Salesforce-ready record and personalized relationship-first scripts"],
    [5, "Review", "Confirm contact channel and product authority"],
    [6, "Execute", "Use approved workflows only after the applicable gates are satisfied"],
], columns=["Step", "Stage", "Rule"]), width="stretch", hide_index=True)

st.warning("This strategy does not itself authorize a product, security, solicitation, advertisement or contact channel. Verified licensing, appointment, registration and NYL approval control execution.")
