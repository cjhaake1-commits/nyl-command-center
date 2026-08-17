from __future__ import annotations

from datetime import date
import streamlit as st

st.set_page_config(page_title="NYL Growth OS", page_icon="◆", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.4rem; max-width: 1500px;}
[data-testid="stMetric"] {background: rgba(255,255,255,.035); border: 1px solid rgba(128,128,128,.22); padding: 14px; border-radius: 12px;}
.hero {padding: 24px 26px; border: 1px solid rgba(128,128,128,.25); border-radius: 16px; margin-bottom: 18px; background: linear-gradient(135deg, rgba(24,53,88,.28), rgba(20,20,25,.08));}
.eyebrow {font-size:.78rem; letter-spacing:.14em; text-transform:uppercase; opacity:.65;}
.hero h1 {margin:.2rem 0 .35rem 0; font-size:2.25rem;}
.hero p {margin:0; opacity:.78; font-size:1.02rem;}
</style>
<div class="hero">
<div class="eyebrow">Personal Growth Operating System • Greater Orlando</div>
<h1>Advisor Growth Command Center</h1>
<p>Prospect intelligence → warm-path development → first touch → pipeline → planning opportunities → implementation → referrals → learning.</p>
</div>
""", unsafe_allow_html=True)

st.caption("Built to demonstrate a full-stack prospecting and execution capability. Future NYL/Salesforce connectivity is an authorized integration layer, not assumed access.")

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Lead reservoir", "Building")
c2.metric("Hot-list target", "20/day")
c3.metric("Weekly touches", "60")
c4.metric("First meetings", "3–4/wk")
c5.metric("Diagnostics", "1–2/wk")

st.subheader("Today’s Operating Flow")
flow = [
    ("1", "Discover", "Public/approved sources, events, referrals, business triggers"),
    ("2", "Score", "Opportunity + warmth + timing + access + strategic fit"),
    ("3", "Warm", "COI paths, shared organizations, trigger context, value-before-ask"),
    ("4", "Engage", "Human-reviewed first-touch brief and compliant outreach"),
    ("5", "Diagnose", "Approved fact-finding; identify documented needs"),
    ("6", "Coordinate", "Specialists, planning resources, underwriting/case support"),
    ("7", "Compound", "Service cadence, introductions, annual reviews, learning loop"),
]
for n,title,desc in flow:
    st.markdown(f"**{n}. {title}** — {desc}")

st.divider()
st.subheader("Practice Intelligence Modules")
left,right = st.columns(2)
with left:
    st.markdown("**Growth & Acquisition**")
    st.write("• Independent public-source lead engine")
    st.write("• Daily ranked Hot List and trigger radar")
    st.write("• Multi-service opportunity matching")
    st.write("• COI / referral relationship graph")
    st.write("• Networking and event pipeline")
    st.write("• Marketing / direct-mail campaign planning")
    st.write("• Warm-path and first-touch preparation")
    st.write("• Lead exports with provenance")

    st.markdown("**Sales Execution**")
    st.write("• Daily War Room and reverse-engineered production goals")
    st.write("• Target → Trigger → Touch → Meet → Diagnose → Design → Implement")
    st.write("• Dated-next-action discipline")
    st.write("• Owner, COI and event sequences")
    st.write("• Conversion and weakest-link analytics")
with right:
    st.markdown("**Planning Opportunity Intelligence**")
    st.write("• Personal and business-owner protection conversations")
    st.write("• Key-person and succession/buy-sell hypotheses")
    st.write("• Retirement and retirement-income conversation flags")
    st.write("• Executive / employee benefit opportunity flags")
    st.write("• Disability and long-term-care conversation flags")
    st.write("• Estate / legacy coordination flags")
    st.write("• Investment/advisory conversation flags where licensed/authorized")

    st.markdown("**Future Enterprise Integration**")
    st.write("• Salesforce/CRM match and deduplication")
    st.write("• Existing-relationship prioritization")
    st.write("• Activity and outcome reconciliation")
    st.write("• Public-intelligence gap fill")
    st.write("• Personal model learns from actual conversion outcomes")

st.divider()
st.subheader("Top-Producer Analytics Roadmap")
roadmap = [
    "Pipeline velocity and stage-aging dashboard",
    "Case-value / expected-production forecasting",
    "Lead-source ROI and conversion by channel",
    "Introductions-per-client and COI referral yield",
    "Appointment quality and diagnostic conversion",
    "Service-category penetration by relationship",
    "90-day review and renewal/service calendar",
    "Event ROI and networking relationship attribution",
    "Territory / industry opportunity heat maps",
    "Scenario planning: required activity for production milestones",
    "Stale-opportunity rescue queue and no-next-action alerts",
    "Morning executive brief: top priorities, risks, meetings and follow-ups",
]
for item in roadmap:
    st.write(f"• {item}")

st.divider()
st.subheader("Control Principles")
st.success("Automate discovery, research, scoring, reminders, preparation and reporting. Keep relationship judgment, needs analysis, recommendations and regulated communications human-led and within approved systems/processes.")
st.caption(f"Command Center build • {date.today().isoformat()}")
