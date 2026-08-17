from __future__ import annotations

from datetime import date
import streamlit as st

st.set_page_config(page_title="Advisor Growth OS", page_icon="◆", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.25rem; padding-bottom: 2rem; max-width: 1450px;}
h1,h2,h3 {letter-spacing:-.02em;}
[data-testid="stMetric"] {background:rgba(255,255,255,.035); border:1px solid rgba(128,128,128,.20); padding:15px 16px; border-radius:14px; box-shadow:0 8px 24px rgba(0,0,0,.06);}
.hero {padding:30px; border:1px solid rgba(128,128,128,.22); border-radius:20px; margin-bottom:20px; background:linear-gradient(135deg,rgba(19,52,84,.42),rgba(15,27,43,.14)); box-shadow:0 14px 40px rgba(0,0,0,.10);}
.eyebrow {font-size:.74rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; opacity:.62;}
.hero h1 {margin:.35rem 0 .45rem; font-size:2.45rem; line-height:1.05;}
.hero p {margin:0; opacity:.78; font-size:1.04rem; max-width:950px;}
.section-card {border:1px solid rgba(128,128,128,.18); border-radius:16px; padding:18px 20px; margin:8px 0 16px; background:rgba(255,255,255,.018);}
.pill {display:inline-block; padding:5px 9px; margin:3px 4px 3px 0; border-radius:999px; border:1px solid rgba(128,128,128,.25); font-size:.78rem; opacity:.82;}
</style>
<div class="hero">
<div class="eyebrow">Advisor Growth Operating System • Greater Orlando</div>
<h1>Growth Command Center</h1>
<p>A unified operating layer for prospect intelligence, relationship development, meeting preparation, pipeline execution, opportunity discovery, production management and continuous learning.</p>
</div>
""", unsafe_allow_html=True)

status1,status2,status3 = st.columns([1,1,2])
status1.success("SYSTEM • ONLINE")
status2.info("LEAD ENGINE • BUILDING")
status3.caption("Future NYL/Salesforce connectivity activates only with authorized access. Public-source intelligence remains independently traceable.")

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Lead Reservoir", "Building", "Continuous")
c2.metric("Daily Priority", "20", "Hot-list target")
c3.metric("Weekly Touches", "60", "Target")
c4.metric("First Meetings", "3–4", "per week")
c5.metric("Diagnostics", "1–2", "per week")

st.subheader("Operating System")
cols = st.columns(4)
modules = [
    ("01", "Discover", "Public sources, referrals, events and business triggers"),
    ("02", "Prioritize", "Opportunity, warmth, timing and strategic-fit scoring"),
    ("03", "Prepare", "Warm paths, research, meeting briefs and value-before-ask"),
    ("04", "Execute", "Touches, meetings, diagnostics and dated next actions"),
    ("05", "Design", "Documented needs, planning paths and specialist coordination"),
    ("06", "Implement", "Case progression, follow-through and service discipline"),
    ("07", "Expand", "Reviews, introductions, COIs and additional documented needs"),
    ("08", "Learn", "Conversion analytics continuously recalibrate priorities"),
]
for i,(num,title,desc) in enumerate(modules):
    with cols[i % 4]:
        st.markdown(f"<div class='section-card'><div class='eyebrow'>{num}</div><h3>{title}</h3><div style='opacity:.72'>{desc}</div></div>", unsafe_allow_html=True)

st.subheader("Intelligence Stack")
left,right = st.columns(2)
with left:
    st.markdown("### Acquisition & Relationship Intelligence")
    st.markdown("<span class='pill'>Public Lead Engine</span><span class='pill'>Trigger Radar</span><span class='pill'>Warm-Path Graph</span><span class='pill'>COI Network</span><span class='pill'>Event Intelligence</span><span class='pill'>Campaign Planning</span><span class='pill'>Lead Provenance</span>", unsafe_allow_html=True)
    st.markdown("### Execution & Coaching")
    st.markdown("<span class='pill'>Daily War Room</span><span class='pill'>First-Touch Briefs</span><span class='pill'>Meeting Intelligence</span><span class='pill'>Pipeline Rescue</span><span class='pill'>Conversion Learning</span><span class='pill'>Production Math</span>", unsafe_allow_html=True)
with right:
    st.markdown("### Opportunity Intelligence")
    st.markdown("<span class='pill'>Protection</span><span class='pill'>Business Owner</span><span class='pill'>Key Person</span><span class='pill'>Succession</span><span class='pill'>Retirement</span><span class='pill'>Executive Benefits</span><span class='pill'>Employee Benefits</span><span class='pill'>Legacy</span><span class='pill'>Advisory*</span>", unsafe_allow_html=True)
    st.markdown("### Enterprise Integration")
    st.markdown("<span class='pill'>CRM Match</span><span class='pill'>Deduplication</span><span class='pill'>Relationship Check</span><span class='pill'>Activity Sync</span><span class='pill'>Gap Analysis</span><span class='pill'>Outcome Feedback</span>", unsafe_allow_html=True)
    st.caption("*Where licensed, registered and authorized; opportunity flags are not recommendations.")

st.subheader("Next-Level Analytics")
roadmap = ["Pipeline velocity & stage aging", "Expected-production forecasting", "Lead-source ROI", "COI/referral yield", "Appointment-quality conversion", "Service-category coverage", "90-day review calendar", "Event ROI", "Territory/industry heat maps", "Production scenario planning", "Stale-opportunity rescue", "Morning executive brief"]
r1,r2,r3 = st.columns(3)
for i,item in enumerate(roadmap):
    [r1,r2,r3][i % 3].write(f"✓ {item}")

st.divider()
st.caption(f"Advisor Growth OS • Build {date.today().isoformat()} • Automate research, prioritization, preparation and reporting; keep regulated judgment and recommendations within approved processes.")
