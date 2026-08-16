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

navigation = st.navigation(
    {
        "NYL Command Center": [war_room, my_strategy],
        "Growth": [prospecting, marketing],
    },
    position="sidebar",
)

navigation.run()
