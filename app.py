from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="NYL Command Center", page_icon="🎯", layout="wide")

war_room = st.Page("pages/1_Daily_War_Room.py", title="Daily War Room", icon="🎯", default=True)
my_strategy = st.Page("pages/4_My_Strategy.py", title="My NYL Strategy", icon="💎")
first_sale = st.Page("pages/5_First_Sale_Program.py", title="First-Sale Program", icon="🚀")
autopilot = st.Page("pages/7_Autopilot.py", title="Sales Autopilot", icon="⚡")
prospect_intel = st.Page("pages/6_Prospect_Intelligence.py", title="Prospect Intelligence", icon="🔎")
prospecting = st.Page("pages/2_Prospecting.py", title="Prospecting & Pipeline", icon="🧭")
marketing = st.Page("pages/3_Marketing.py", title="Marketing Command Center", icon="📣")
interview = st.Page("pages/8_Interview_Ace.py", title="Final Interview Ace", icon="🃏")

navigation = st.navigation(
    [
        war_room,
        my_strategy,
        first_sale,
        autopilot,
        prospect_intel,
        prospecting,
        marketing,
        interview,
    ],
    position="sidebar",
)

navigation.run()
