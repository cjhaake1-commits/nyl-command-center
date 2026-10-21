from __future__ import annotations

from urllib.parse import quote_plus

import streamlit as st


def _search_link(base: str, query: str) -> str:
    return f"{base}{quote_plus(query.strip())}" if query.strip() else base


def render_business_networking_desk() -> None:
    st.title("Business & Networking Desk")
    st.caption("A quick, source-first toolkit for preparing before a call or entering a networking room with informed curiosity.")

    sunbiz_search = "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName"
    sunbiz_officers = "https://search.sunbiz.org/Inquiry/CorporationSearch/ByOfficerOrRegisteredAgent"
    sunbiz_recent = "https://dos.fl.gov/sunbiz/search/"
    st.subheader("Florida Sunbiz • official business registry")
    st.write("Search active and historical Florida corporations, LLCs, partnerships, fictitious names, officers, and registered agents. Verify legal name, status, document details, and filing dates on the official record.")
    entity = st.text_input("Business or entity name", key="sunbiz_entity_search", placeholder="Enter the business name")
    person = st.text_input("Officer or registered agent (optional)", key="sunbiz_officer_search", placeholder="Enter a public business-related name")
    a, b, c = st.columns(3)
    a.link_button("Search entity name", _search_link(sunbiz_search, entity), use_container_width=True)
    b.link_button("Search officer / registered agent", _search_link(sunbiz_officers, person), use_container_width=True)
    c.link_button("Sunbiz records & filing guidance", sunbiz_recent, use_container_width=True)
    st.caption("New entity filings do not establish that a business is operating, that a named person is a decision maker, or that it has a planning need. Confirm independently and follow firm policy before outreach.")

    st.divider()
    st.subheader("Florida new-business discovery")
    st.markdown("Use county and state sources to locate recent formation or expansion signals. For a new LLC, check the filing date and active status, then look for independent operating evidence—website, hiring, permits, opening announcement, or business-directory listing. Treat each as a research candidate, not a qualified prospect.")
    regions = {
        "Orange County": {
            "sunbiz": "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName",
            "permits": "https://fasttrack.ocfl.net/OnlineServices/Permit_Main.aspx",
            "business": "https://business.orlando.org/list/",
        },
        "Seminole County": {
            "sunbiz": "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName",
            "permits": "https://www.seminolecountyfl.gov/departments-services/development-services/building/",
            "business": "https://business.seminolebusiness.org/list/",
        },
        "Osceola County": {
            "sunbiz": "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName",
            "permits": "https://permits.osceola.org/CitizenAccess/",
            "business": "https://business.kissimmeechamber.com/list/",
        },
        "Lake County": {
            "sunbiz": "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName",
            "permits": "https://www.lakecountyfl.gov/building-services",
            "business": "https://business.clermontflchamber.com/list/",
        },
    }
    selected = st.selectbox("Target county", list(regions))
    links = regions[selected]
    l1, l2, l3, l4 = st.columns(4)
    l1.link_button("Sunbiz search", links["sunbiz"], use_container_width=True)
    l2.link_button("County permits", links["permits"], use_container_width=True)
    l3.link_button("Local business directory", links["business"], use_container_width=True)
    l4.link_button("Google Maps search", _search_link("https://www.google.com/maps/search/", selected + " new businesses"), use_container_width=True)

    st.divider()
    st.subheader("Business research quick links")
    resources = [
        ("SEC EDGAR", "Public-company and investment-company filings. Use filings for company context; do not infer a private company's needs from unrelated data.", "https://www.sec.gov/edgar/search/"),
        ("SEC Investment Adviser Public Disclosure", "Check adviser firm/professional public disclosures when relevant; not a referral or endorsement.", "https://adviserinfo.sec.gov/"),
        ("U.S. Census Business Builder", "Industry, demographic, and local business context at area level.", "https://www.census.gov/data/data-tools/cbb.html"),
        ("SBA local assistance", "Find small-business support organizations and public programs; useful for community networking.", "https://www.sba.gov/local-assistance"),
        ("Orlando Economic Partnership company directory", "Regional companies, industries, and publicly listed contacts.", "https://orlando.org/companies/"),
        ("West Orange Chamber directory", "Member businesses and owner networking in west Orange County.", "https://business.wochamber.com/list/search?o=&q=all"),
        ("Winter Park Chamber directory", "Businesses and professional network in Winter Park/Maitland.", "https://business.winterpark.org/list/"),
        ("City of Orlando local business search", "Certified small/local business directory by company and service area.", "https://www.orlando.gov/Our-Government/Departments-Offices/Economic-Development/Business-Development/Small-Business-Enterprise-Program/Search-for-a-Certified-Small-or-Local-Business"),
        ("ZoomInfo (future)", "Connect only through an NYL-approved account/API and authorized use terms; store credentials in deployment secrets, never in code.", "https://www.zoominfo.com/"),
    ]
    for name, description, url in resources:
        with st.container(border=True):
            col1, col2 = st.columns([4, 1])
            col1.markdown(f"**{name}**  \n{description}")
            col2.link_button("Open", url, use_container_width=True)

    st.divider()
    st.subheader("Walk-in or phone prep • 30 seconds")
    st.markdown("1. **Notice:** What confirmed detail, work, milestone, or industry issue can I mention?\n2. **Ask:** What are you focused on right now?\n3. **Listen:** What is changing, important, or taking time?\n4. **Relate:** Share one short, relevant observation or your role only if it helps.\n5. **Permission:** Would it be useful to continue this another time?")
    st.info("Aim for curiosity and usefulness. Avoid showing off research, reciting filings, asking personal financial questions in a public setting, or turning an introduction into a product pitch.")
    st.markdown("**Easy openers**")
    openers = [
        ("Business owner", "“I saw the company recently expanded / opened [verify first]. How has that changed what you’re focused on?”"),
        ("Professional / referral partner", "“What kinds of clients or business transitions are taking most of your attention this year?”"),
        ("Event host", "“What brought you into this group, and what would make tonight valuable for you?”"),
        ("Follow-up", "“I enjoyed hearing about [their stated priority]. Would you be open to a short follow-up next week?”"),
    ]
    st.dataframe([{"Situation": title, "Conversation opener": line} for title, line in openers], hide_index=True, width="stretch")

    st.divider()
    st.subheader("Lead quality gate")
    st.markdown("Before treating a business as a prospect, require: **cause** (specific verified event), **identity** (right owner/decision maker confirmed), **operating evidence** (not just a legal entity), **public professional contact channel**, **source/date**, **dedupe check**, and **next action**. Hold any record that fails a gate. Do not collect personal or financial details here.")
    st.caption("ZoomInfo is reserved for a future approved integration. This page does not scrape Sunbiz in bulk, automate outreach, save prospect records, or import data into Salesforce.")
