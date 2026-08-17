from __future__ import annotations

from datetime import date
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Prospect Intelligence", page_icon="🔎", layout="wide")
st.title("Prospect Intelligence Engine")
st.caption("Greater Orlando prospect prioritization, trigger detection, COI mapping, and daily next-best-action planning.")

st.info("Uses business/public professional signals for prospecting. Do not infer sensitive traits or treat public-data scores as proof of a financial need. NYL-approved systems remain the system of record once connected.")

with st.sidebar:
    st.header("Radar Controls")
    territory = st.selectbox("Territory", ["Greater Orlando", "Winter Park / Maitland", "Lake Nona", "Windermere / Dr. Phillips", "Seminole County"])
    min_score = st.slider("Minimum opportunity score", 0, 100, 60)
    show_n = st.slider("Daily hot list size", 5, 50, 20)

st.subheader("Today's Opportunity Radar")
a,b,c,d = st.columns(4)
a.metric("Hot prospects", "20")
b.metric("New triggers", "0", help="Populates when approved/public data feeds are connected.")
c.metric("COI opportunities", "0")
d.metric("Follow-ups due", "0")

st.subheader("Daily Hot List")
st.caption("The production version will rank real records from connected public/approved data feeds. Until then this table is the scoring workspace, not fabricated lead data.")
columns = ["Prospect", "Type", "Area", "Score", "Trigger", "Why now", "Conversation angle", "Last touch", "Next action", "Source"]
if "hot_list" not in st.session_state:
    st.session_state.hot_list = pd.DataFrame(columns=columns)

edited = st.data_editor(st.session_state.hot_list, num_rows="dynamic", width="stretch", hide_index=True, key="hot_list_editor")
if st.button("Save Hot List", type="primary"):
    st.session_state.hot_list = edited
    st.success("Hot list saved for this session. Persistent storage can be wired to the existing PostgreSQL layer next.")

st.subheader("Opportunity Scoring Model")
weights = pd.DataFrame([
    ["Recent business/life-cycle trigger", 25, "Public business event that creates a timely reason to talk"],
    ["Business-owner / executive relevance", 20, "Role aligns with business-owner or executive planning conversations"],
    ["Affluent-market fit", 15, "Non-sensitive public geographic/property/professional signals"],
    ["Employee / organizational scale", 15, "Company scale supports employer/executive planning hypotheses"],
    ["COI / referral proximity", 10, "Potential warm path through a center of influence"],
    ["Engagement / prior touch", 10, "Observed response or prior interaction"],
    ["Freshness", 5, "Signal is recent enough to act on"],
], columns=["Signal", "Max points", "Interpretation"])
st.dataframe(weights, width="stretch", hide_index=True)

st.subheader("Trigger Detector")
trigger_types = ["New business registration", "Hiring / growth", "Executive change", "New location", "Commercial property event", "Funding / acquisition", "Succession indicator", "Employee-count milestone", "Public professional change"]
selected = st.multiselect("Signals to monitor", trigger_types, default=trigger_types)
st.caption(f"Monitoring configuration: {len(selected)} trigger categories in {territory}. Data connectors are intentionally separated from scoring so Salesforce can be plugged in later.")

st.subheader("Centers of Influence")
coi = pd.DataFrame(columns=["Name / Firm", "COI type", "Area", "Relationship strength", "Potential introductions", "Last touch", "Next action"])
st.data_editor(coi, num_rows="dynamic", width="stretch", hide_index=True, key="coi_editor")
st.caption("Suggested COI categories: CPAs, estate/business attorneys, commercial real-estate professionals, bankers, benefits professionals, mortgage professionals, and other firm-approved referral relationships.")

st.subheader("Prospect Radar")
st.write("Geographic clustering is ready for a future map layer. Add coordinates only from lawful public/approved business data; avoid exposing precise private-residence locations in the dashboard.")

st.subheader("Next Best Action")
prospect_name = st.text_input("Prospect or company")
trigger = st.selectbox("Observed trigger", ["None selected"] + trigger_types)
relationship = st.selectbox("Relationship", ["Cold", "Warm", "COI introduction", "Existing relationship - verify in CRM later"])
if st.button("Generate action plan"):
    if prospect_name.strip():
        st.markdown(f"**Priority review:** {prospect_name}\n\n**Observed trigger:** {trigger}\n\n**Relationship:** {relationship}\n\n**Recommended workflow:** verify the public signal → check internal eligibility/relationship status when CRM access is approved → choose a firm-approved conversation angle → log the touch → schedule a dated next action.")
    else:
        st.warning("Enter a prospect or company first.")

st.subheader("Conversion Learning")
conversion = pd.DataFrame(columns=["Date", "Segment", "Source", "Touches", "Conversations", "Appointments", "Placed sales", "Referrals"])
st.data_editor(conversion, num_rows="dynamic", width="stretch", hide_index=True, key="conversion_editor")
st.caption("As outcomes accumulate, this becomes the feedback loop for recalibrating scores from your actual conversion history instead of generic assumptions.")

st.subheader("Future CRM / Salesforce Bridge")
st.success("Connector boundary is reserved: match/dedupe → relationship check → permitted policy/client context → next-best-opportunity ranking → activity sync. No Salesforce credentials are required now.")
st.code("PUBLIC/APPROVED DATA → PROSPECT SCORE → HOT LIST → OUTREACH → APPOINTMENT → [FUTURE NYL CRM/SALESFORCE] → OUTCOME → SCORE LEARNING", language="text")

st.caption(f"Radar configuration updated {date.today().isoformat()} • Minimum score {min_score} • Daily list {show_n}")
