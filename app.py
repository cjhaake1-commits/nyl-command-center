from __future__ import annotations

import streamlit as st

war_room = st.Page(
    "pages/1_Daily_War_Room.py",
    title="Daily War Room",
    icon="🎯",
    default=True,
)
prospecting = st.Page(
    "pages/2_Prospecting.py",
    title="Prospecting & Pipeline",
    icon="🧭",
)
marketing = st.Page(
    "pages/3_Marketing.py",
    title="Marketing Command Center",
    icon="📣",
)
my_strategy = st.Page(
    "pages/4_My_Strategy.py",
    title="My NYL Strategy",
    icon="💎",
)
first_sale = st.Page(
    "pages/5_First_Sale_Program.py",
    title="First-Sale Program",
    icon="🚀",
)
operating_system = st.Page(
    "pages/6_Operating_System.py",
    title="Operating System",
    icon="🧰",
)
autopilot = st.Page(
    "pages/7_Autopilot.py",
    title="Sales Autopilot",
    icon="⚡",
)
interview = st.Page(
    "pages/8_Interview_Ace.py",
    title="Final Interview Ace",
    icon="🃏",
)

navigation = st.navigation(
    {
        "Tomorrow": [interview],
        "NYL Command Center": [war_room, my_strategy, first_sale, operating_system, autopilot],
        "Growth": [prospecting, marketing],
    },
    position="sidebar",
)

navigation.run()
