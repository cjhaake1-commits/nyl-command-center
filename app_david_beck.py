from __future__ import annotations

import streamlit as st

from core.branding import apply_brand_theme
from core.rep_branding import sidebar_brand
from core.rep_profile import APP_TITLE

BUILD_STAMP = "2026-09-03 20:45 ET • PAUL BECK"

st.set_page_config(page_title=APP_TITLE, page_icon="📈", layout="wide", initial_sidebar_state="expanded")
apply_brand_theme()
sidebar_brand()

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {display:flex!important;flex-direction:column!important;background:linear-gradient(180deg,#05080c 0%,#090d12 100%)!important;}
    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {order:-100!important;flex:0 0 auto!important;padding-top:.35rem!important;}
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {order:10!important;flex:1 1 auto!important;padding-top:.3rem!important;}
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] > div:has(.brand-lockup) {order:-100!important;}
    [data-testid="stSidebarNav"] ul {gap:2px!important;}
    [data-testid="stSidebarNav"] li > div {color:#d7a449!important;font-size:.68rem!important;letter-spacing:.14em!important;font-weight:800!important;text-transform:uppercase!important;}
    [data-testid="stSidebarNav"] a {border-radius:10px!important;margin:2px 7px!important;}
    [data-testid="stSidebarNav"] a[aria-current="page"] {background:linear-gradient(90deg,rgba(215,164,73,.18),rgba(215,164,73,.035))!important;border-left:2px solid #d7a449!important;}
    @media (max-width:760px) {section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]{padding-top:.1rem!important}.brand-lockup{margin-bottom:.2rem!important;padding-bottom:.65rem!important}.brand-person{margin-top:.55rem!important}.brand-sidebar-note{margin-top:.55rem!important}}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.caption(BUILD_STAMP)

executive = st.Page("pages/0_Executive_Command_Center.py", title="Command Center", icon="📈", default=True)
war_room = st.Page("pages/1_Daily_War_Room.py", title="Daily War Room", icon="🎯")
prospect_discovery = st.Page("pages/2A_Prospect_Discovery.py", title="Prospect Discovery", icon="🔎")
prospecting = st.Page("pages/2_Prospecting.py", title="Prospecting & Pipeline", icon="🧭")
lead_lists = st.Page("pages/9_Lead_Lists.py", title="Lead Lists & Export", icon="📋")
opportunity = st.Page("pages/12_Opportunity_Radar.py", title="Opportunity Radar", icon="📡")
marketing = st.Page("pages/3_Marketing.py", title="Marketing Command Center", icon="📣")
influencer_network = st.Page("pages/3A_Influencer_Network.py", title="Influencer & Referral Network", icon="🤝")
linkedin_network = st.Page("pages/3B_LinkedIn_Network.py", title="LinkedIn Network", icon="🔗")
mailing = st.Page("pages/11_Mailing_Targeting.py", title="Mailing & Targeting", icon="📬")
prospect_intel = st.Page("pages/13_Prospect_Intelligence.py", title="Prospect Intelligence", icon="🧠")
meeting_intel = st.Page("pages/10_Meeting_Intelligence.py", title="Meeting Intelligence", icon="🎙️")
first_sale = st.Page("pages/5_First_Sale_Program.py", title="First-Sale Program", icon="🚀")
autopilot = st.Page("pages/7_Autopilot.py", title="Sales Autopilot", icon="⚡")
interview = st.Page("pages/8_Interview_Ace.py", title="Interview / Presentation", icon="🃏")
my_strategy = st.Page("pages/4_My_Strategy.py", title="Practice Strategy", icon="💎")
make_request = st.Page("pages/14_Make_A_Request.py", title="Make a Request", icon="📝")

navigation = st.navigation(
    {
        "COMMAND": [executive, war_room],
        "PROSPECTING": [prospect_discovery, prospecting, lead_lists, opportunity],
        "MARKETING & NETWORK": [marketing, influencer_network, linkedin_network, mailing],
        "INTELLIGENCE": [prospect_intel, meeting_intel],
        "EXECUTION": [first_sale, autopilot, interview],
        "PRACTICE": [my_strategy],
        "SUPPORT": [make_request],
    },
    position="sidebar",
)

navigation.run()
