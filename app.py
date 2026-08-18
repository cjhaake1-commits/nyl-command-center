from __future__ import annotations

import streamlit as st

from core.branding import apply_brand_theme, sidebar_brand

st.set_page_config(page_title="Chris Haake Command Center", page_icon="◆", layout="wide")
apply_brand_theme()
sidebar_brand()

executive = st.Page("pages/0_Executive_Command_Center.py", title="COMMAND CENTER", icon="📈", default=True)
war_room = st.Page("pages/1_Daily_War_Room.py", title="Daily War Room", icon="🎯")
lead_lists = st.Page("pages/9_Lead_Lists.py", title="LEAD LISTS - EXPORT", icon="📋")
mailing = st.Page("pages/11_Mailing_Targeting.py", title="MAILING & TARGETING", icon="📬")
opportunity = st.Page("pages/12_Opportunity_Radar.py", title="OPPORTUNITY RADAR", icon="📡")
prospect_intel = st.Page("pages/6_Prospect_Intelligence.py", title="Prospect Intelligence", icon="🔎")
meeting_intel = st.Page("pages/10_Meeting_Intelligence.py", title="MEETING INTELLIGENCE", icon="🎙️")
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
    [
        executive,
        war_room,
        lead_lists,
        mailing,
        opportunity,
        prospect_intel,
        meeting_intel,
        prospecting,
        prospect_discovery,
        my_strategy,
        first_sale,
        autopilot,
        marketing,
        influencer_network,
        linkedin_network,
        interview,
    ],
    position="sidebar",
)

navigation.run()
