from __future__ import annotations

import streamlit as st

from core.branding import apply_brand_theme, sidebar_brand

st.set_page_config(page_title="Chris Haake Command Center", page_icon="◆", layout="wide")
apply_brand_theme()
sidebar_brand()

executive = st.Page("pages/0_Executive_Command_Center.py", title="Command Center", icon="📈", default=True)
war_room = st.Page("pages/1_Daily_War_Room.py", title="Daily War Room", icon="🎯")
lead_lists = st.Page("pages/9_Lead_Lists.py", title="Lead Lists & Export", icon="📋")
mailing = st.Page("pages/11_Mailing_Targeting.py", title="Mailing & Targeting", icon="📬")
opportunity = st.Page("pages/12_Opportunity_Radar.py", title="Opportunity Radar", icon="📡")
prospect_intel = st.Page("pages/6_Prospect_Intelligence.py", title="Prospect Intelligence", icon="🔎")
meeting_intel = st.Page("pages/10_Meeting_Intelligence.py", title="Meeting Intelligence", icon="🎙️")
prospecting = st.Page("pages/2_Prospecting.py", title="Prospecting & Pipeline", icon="🧭")
prospect_discovery = st.Page("pages/2A_Prospect_Discovery.py", title="Prospect Discovery", icon="🎯")
my_strategy = st.Page("pages/4_My_Strategy.py", title="Practice Strategy", icon="💎")
first_sale = st.Page("pages/5_First_Sale_Program.py", title="First-Sale Program", icon="🚀")
autopilot = st.Page("pages/7_Autopilot.py", title="Sales Autopilot", icon="⚡")
marketing = st.Page("pages/3_Marketing.py", title="Marketing Command Center", icon="📣")
influencer_network = st.Page("pages/3A_Influencer_Network.py", title="Influencer & Referral Network", icon="📱")
linkedin_network = st.Page("pages/3B_LinkedIn_Network.py", title="LinkedIn Network", icon="🔗")
interview = st.Page("pages/8_Interview_Ace.py", title="Interview / Presentation", icon="🃏")

navigation = st.navigation(
    {
        "COMMAND": [executive, war_room],
        "PROSPECTING": [prospect_discovery, prospecting, lead_lists, opportunity],
        "MARKETING & NETWORK": [marketing, influencer_network, linkedin_network, mailing],
        "INTELLIGENCE": [prospect_intel, meeting_intel],
        "EXECUTION": [first_sale, autopilot, interview],
        "PRACTICE": [my_strategy],
    },
    position="sidebar",
)

navigation.run()
