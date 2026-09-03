from __future__ import annotations

import streamlit as st

from core.branding import apply_brand_theme, brand_hero
from core.rep_branding import sidebar_brand
from core.rep_profile import REP_NAME, TERRITORY_LABEL

st.set_page_config(page_title=f"LinkedIn Network | {REP_NAME}", page_icon="🔗", layout="wide")
apply_brand_theme()
sidebar_brand()

brand_hero(
    "LinkedIn Network",
    "A professional networking workspace for researching prospects, verifying profiles and preparing relationship-first outreach.",
    f"{REP_NAME} Command Center",
)

c1, c2 = st.columns(2)
with c1:
    st.metric("Primary Market", TERRITORY_LABEL)
with c2:
    st.metric("Workflow", "Research → Connect")

st.subheader("Prospect LinkedIn Workspace")
profile_url = st.text_input("Prospect LinkedIn profile URL", placeholder="https://www.linkedin.com/in/...")
if profile_url.strip().startswith("https://www.linkedin.com/"):
    st.link_button("Open prospect on LinkedIn", profile_url.strip(), width="stretch")

q1, q2, q3 = st.columns(3)
first_name = q1.text_input("First name")
last_name = q2.text_input("Last name")
context = q3.text_input("Company / role / local context")
if first_name or last_name:
    search_query = "+".join(x.replace(" ", "+") for x in [first_name, last_name, context] if x.strip())
    st.link_button("Search LinkedIn", f"https://www.linkedin.com/search/results/people/?keywords={search_query}", width="stretch")

st.info("Paul's personal LinkedIn profile has not been configured, so this page intentionally does not show Chris Haake's profile or identity.")
st.caption("No automated scraping or bulk messaging. Use public professional context as research, not as proof of financial need.")
