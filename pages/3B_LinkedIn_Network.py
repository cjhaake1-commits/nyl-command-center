from __future__ import annotations

import streamlit as st

from core.branding import apply_brand_theme, brand_hero, sidebar_brand

st.set_page_config(page_title="LinkedIn Network | Chris Haake", page_icon="🔗", layout="wide")
apply_brand_theme()
sidebar_brand()

brand_hero(
    "LinkedIn Network",
    "A professional networking workspace for researching prospects, opening verified profiles, and preparing compliant relationship-first outreach.",
    "Chris Haake Command Center",
)

PROFILE_URL = "https://www.linkedin.com/in/christopher-haake-171a4b34"

c1, c2, c3 = st.columns([1.25, 1, 1])
with c1:
    st.markdown('<div class="linkedin-card"><div class="linkedin-badge">LINKEDIN PROFILE</div><h3>Chris Haake</h3><p>Primary LinkedIn identity attached to this Command Center. Headshot intentionally omitted until the new professional portrait is ready.</p></div>', unsafe_allow_html=True)
    st.link_button("Open Chris Haake on LinkedIn", PROFILE_URL, width="stretch")
with c2:
    st.metric("Workflow", "Research → Connect")
    st.caption("Use LinkedIn as a warm-path research layer, not a bulk outreach engine.")
with c3:
    st.metric("Primary Market", "Central Florida")
    st.caption("Prioritize mutual context, local communities, business triggers and COI relationships.")

st.subheader("Prospect LinkedIn Workspace")
st.caption("Paste a prospect's public LinkedIn URL or use LinkedIn search to verify professional context before outreach.")
profile_url = st.text_input("Prospect LinkedIn profile URL", placeholder="https://www.linkedin.com/in/...")
if profile_url.strip().startswith("https://www.linkedin.com/"):
    st.link_button("Open prospect on LinkedIn", profile_url.strip(), width="stretch")

q1, q2, q3 = st.columns(3)
first_name = q1.text_input("First name")
last_name = q2.text_input("Last name")
context = q3.text_input("Company / role / Central Florida context")

if first_name or last_name:
    search_query = "+".join(x.replace(" ", "+") for x in [first_name, last_name, context] if x.strip())
    st.link_button("Search LinkedIn", f"https://www.linkedin.com/search/results/people/?keywords={search_query}", width="stretch")

st.divider()
st.subheader("Relationship Prep")
prep1, prep2 = st.columns(2)
with prep1:
    st.markdown("**Before connecting**")
    st.markdown("- Confirm the correct professional identity\n- Identify a legitimate local/business connection\n- Note a current public trigger or shared community\n- Prefer introductions and relevant context over cold pitching")
with prep2:
    st.markdown("**Compliance boundary**")
    st.markdown("- No automated scraping or bulk messaging\n- No assumptions about private finances\n- Use NYL-approved communications and advertising processes\n- Treat public profile information as research context, not a financial-needs determination")

st.info("The current LinkedIn connection available to this workspace supports professional profile discovery/search. It does not provide unrestricted inbox automation, connection-request automation, profile scraping, or posting from this Streamlit app. The page is intentionally designed around the supported research-and-open-profile workflow.")
