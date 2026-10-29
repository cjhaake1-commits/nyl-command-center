from __future__ import annotations

import streamlit as st

from core.branding import apply_brand_theme
from core.rep_branding import sidebar_brand
from core.rep_profile import APP_TITLE

st.set_page_config(page_title=APP_TITLE, page_icon="📈", layout="wide", initial_sidebar_state="expanded")
apply_brand_theme()
sidebar_brand()

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {display:flex!important;flex-direction:column!important;}
    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {order:-100!important;flex:0 0 auto!important;padding-top:.35rem!important;}
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {order:10!important;flex:1 1 auto!important;padding-top:.3rem!important;}
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] > div:has(.brand-lockup) {order:-100!important;}
    @media (max-width:760px) {section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]{padding-top:.1rem!important}.brand-lockup{margin-bottom:.2rem!important;padding-bottom:.65rem!important}.brand-person{margin-top:.55rem!important}.brand-sidebar-note{margin-top:.55rem!important}}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.caption("Devin Lynch tenant • Central Florida / Ocala")
st.sidebar.caption("Shared team calendar and prospect pipeline")

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
event_schedule = st.Page("pages/26_Event_Schedule.py", title="Event Schedule", icon="🗓️")
group_affinity = st.Page("pages/14_Group_Affinity_Benefits.py", title="Group / Affinity Benefits", icon="🤝")
community_prospecting = st.Page("pages/27_Community_Prospecting.py", title="Community Prospecting", icon="🌱")
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
market_monitor = st.Page("pages/20_Market_Monitor.py", title="Market Monitor", icon="📊")
subject_brief = st.Page("pages/21_Quick_Subject_Briefing.py", title="Quick Subject Briefing", icon="🔍")
business_desk = st.Page("pages/22_Business_Networking_Desk.py", title="Business & Networking Desk", icon="🏢")
quarterback = st.Page("pages/23_Relationship_Quarterback.py", title="Relationship Quarterback", icon="🏈")
series_7 = st.Page("pages/24_Series_7_Study_Guide.py", title="Series 7 Study Guide", icon="📚")
series_65 = st.Page("pages/25_Series_65_Study_Guide.py", title="Series 65 Study Guide", icon="📖")

navigation = st.navigation(
    {
        "COMMAND": [executive, growth_plan, war_room, quarterback],
        "COACHING": [sales_coach],
        "MARKETS & ECONOMY": [market_monitor],
        "PROSPECTING": [prospect_discovery, prospecting, lead_lists, opportunity, event_prospecting, event_schedule, group_affinity, community_prospecting],
        "MARKETING & NETWORK": [marketing, influencer_network, linkedin_network, mailing],
        "INTELLIGENCE": [prospect_intel, meeting_intel, subject_brief, business_desk],
        "EXECUTION": [rollover_playbook, first_sale, autopilot, interview, practice_lab],
        "STUDY DESK": [series_7, series_65],
        "PRACTICE": [my_strategy],
    },
    position="sidebar",
)

navigation.run()
