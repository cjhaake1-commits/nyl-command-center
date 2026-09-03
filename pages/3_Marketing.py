from __future__ import annotations

import pandas as pd
import streamlit as st

from core.rep_profile import REP_NAME, TERRITORY_LABEL, TERRITORY_ZIP, TERRITORY_RADIUS_MILES

st.set_page_config(page_title=f"Marketing Command Center | {REP_NAME}", page_icon="📣", layout="wide")
st.title("Marketing Command Center")
st.caption(f"{REP_NAME} • {TERRITORY_LABEL} • local visibility, networking and campaign planning")

st.warning("Insurance/securities advertising, direct mail, social posts, landing pages and event invitations remain draft-only until the applicable NYL/firm review and legal requirements are satisfied.")

st.subheader("Territory")
st.dataframe(pd.DataFrame([{
    "Center ZIP": TERRITORY_ZIP,
    "Market": "Simi Valley, California",
    "Radius": f"{TERRITORY_RADIUS_MILES} miles",
    "Planning rule": "Use verified local public sources; do not reuse Central Florida market data",
}]), width="stretch", hide_index=True)

st.subheader("90-Day Relationship Campaign Builder")
audience = st.selectbox("Audience", ["Business owners", "Executives / professionals", "Centers of influence", "Professional practices", "Growing employers"])
theme = st.selectbox("Education / relationship theme", ["Business continuity", "Protection planning", "Retirement education", "Succession / ownership planning", "Executive & employee benefits", "General relationship building"])
weekly_budget = st.number_input("Illustrative weekly budget ($)", min_value=0, value=250, step=50)

st.dataframe(pd.DataFrame([
    ["Weeks 1-2", "Build verified local list and COI map", "No outreach until channel/authorization review"],
    ["Weeks 3-4", "Prepare approved educational content and event/networking plan", "Keep custom materials in draft/HOLD"],
    ["Weeks 5-8", "Measure responses, introductions and meetings", "Track source and consent status"],
    ["Weeks 9-12", "Double down on highest-quality relationship sources", "Do not optimize on sensitive individual traits"],
], columns=["Window", "Focus", "Control"]), width="stretch", hide_index=True)

st.markdown(f"**Current planning scenario:** {audience} • {theme} • ${weekly_budget:,.0f}/week illustrative budget.")
st.info("Use Make a Request to add verified local organizations, events, approved product themes or additional campaign capabilities for Paul.")
