from __future__ import annotations

import streamlit as st

from core.branding import apply_brand_theme, sidebar_brand

st.set_page_config(page_title="Chris Haake Command Center", page_icon="📈", layout="wide")
apply_brand_theme()
sidebar_brand()

# Streamlit's multipage navigation is rendered ahead of normal sidebar content by
# default. Force the Chris Haake identity block above navigation on both desktop
# and the mobile sidebar drawer so branding is visible immediately, not below the fold.
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
        display: flex !important;
        flex-direction: column !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
        order: -100 !important;
        flex: 0 0 auto !important;
        padding-top: 0.35rem !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        order: 10 !important;
        flex: 1 1 auto !important;
    }

    /* Fallback for Streamlit builds where the user-content wrapper changes. */
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] > div:has(.brand-lockup) {
        order: -100 !important;
    }

    /* Keep the identity panel compact enough to remain visible on smaller phones. */
    @media (max-width: 760px) {
        section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
            padding-top: 0.15rem !important;
        }
        section[data-testid="stSidebar"] .brand-lockup {
            margin-bottom: 0.25rem !important;
            padding-top: 0.25rem !important;
            padding-bottom: 0.75rem !important;
        }
        section[data-testid="stSidebar"] .brand-person {
            margin-top: 0.65rem !important;
        }
        section[data-testid="stSidebar"] .brand-sidebar-note {
            margin-top: 0.6rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

executive = st.Page("pages/0_Executive_Command_Center.py", title="Command Center", icon="📈", default=True)
growth_plan = st.Page("pages/17_First_Year_Growth_Plan.py", title="First-Year $1M Growth Plan", icon="🏆")
war_room = st.Page("pages/1_Daily_War_Room.py", title="Daily War Room", icon="🎯")
lead_lists = st.Page("pages/9_Lead_Lists.py", title="Lead Lists & Export", icon="📋")
mailing = st.Page("pages/11_Mailing_Targeting.py", title="Mailing & Targeting", icon="📬")
opportunity = st.Page("pages/12_Opportunity_Radar.py", title="Opportunity Radar", icon="📡")
prospect_intel = st.Page("pages/13_Prospect_Intelligence.py", title="Prospect Intelligence", icon="🔎")
meeting_intel = st.Page("pages/10_Meeting_Intelligence.py", title="Meeting Intelligence", icon="🎙️")
prospecting = st.Page("pages/2_Prospecting.py", title="Prospecting & Pipeline", icon="🧭")
prospect_discovery = st.Page("pages/2A_Prospect_Discovery.py", title="Prospect Discovery", icon="🎯")
event_prospecting = st.Page("pages/15_Event_Prospecting.py", title="Event Prospecting", icon="🤝")
group_affinity = st.Page("pages/14_Group_Affinity_Benefits.py", title="Group / Affinity Benefits", icon="🤝")
my_strategy = st.Page("pages/4_My_Strategy.py", title="Practice Strategy", icon="💎")
rollover_playbook = st.Page("pages/16_Rollover_Playbook.py", title="401(k) Rollover Playbook", icon="📘")
first_sale = st.Page("pages/5_First_Sale_Program.py", title="First-Sale Program", icon="🚀")
autopilot = st.Page("pages/7_Autopilot.py", title="Sales Autopilot", icon="⚡")
marketing = st.Page("pages/3_Marketing.py", title="Marketing Command Center", icon="📣")
influencer_network = st.Page("pages/3A_Influencer_Network.py", title="Influencer & Referral Network", icon="📱")
linkedin_network = st.Page("pages/3B_LinkedIn_Network.py", title="LinkedIn Network", icon="🔗")
interview = st.Page("pages/8_Interview_Ace.py", title="Interview / Presentation", icon="🃏")
practice_lab = st.Page("pages/18_Practice_Process_Lab.py", title="Practice & Process Lab", icon="🎭")
sales_coach = st.Page("pages/19_Sales_Coach.py", title="Sales Coach", icon="🧭")

navigation = st.navigation(
    {
        "COMMAND": [executive, growth_plan, war_room],
        "COACHING": [sales_coach],
        "PROSPECTING": [prospect_discovery, prospecting, lead_lists, opportunity, event_prospecting, group_affinity],
        "MARKETING & NETWORK": [marketing, influencer_network, linkedin_network, mailing],
        "INTELLIGENCE": [prospect_intel, meeting_intel],
        "EXECUTION": [rollover_playbook, first_sale, autopilot, interview, practice_lab],
        "PRACTICE": [my_strategy],
    },
    position="sidebar",
)

navigation.run()
