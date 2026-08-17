from __future__ import annotations

from datetime import date
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Prospect Intelligence", page_icon="🔎", layout="wide")
st.title("Prospect Intelligence Engine")
st.caption("Greater Orlando prospect prioritization, pre-contact warming, trigger detection, COI mapping, and daily next-best-action planning.")

st.info("Uses lawful business/public professional signals for prospecting. Public-data scores are hypotheses, not proof of a financial need. External messages remain human-reviewed and NYL-approved systems become the system of record when connected.")

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

st.subheader("Pre-Contact Warmth Engine")
st.caption("Goal: do the research and relationship work before the first ask so a cold name can become a contextual, introduced, event-connected, or otherwise warmer first conversation.")
w1,w2,w3,w4 = st.columns(4)
w1.metric("Cold", "0")
w2.metric("Contextual", "0")
w3.metric("Warm", "0")
w4.metric("Hot / engaged", "0")

warmth_rules = pd.DataFrame([
    ["Verified timely trigger", 20, "A sourced business event creates a legitimate reason to contact now."],
    ["Direct COI introduction available", 30, "Best warming path: trusted person can introduce you."],
    ["Shared organization / event", 15, "Same chamber, ACG/BNI/industry event, or other genuine context."],
    ["Prior relationship / permitted connection", 25, "Existing professional relationship or permitted prior contact."],
    ["Prospect engaged publicly with relevant topic", 10, "Use only genuine public professional engagement; do not manufacture familiarity."],
    ["Company-specific relevance verified", 10, "One accurate public fact supports a useful business question."],
    ["Inbound response / requested follow-up", 35, "Prospect has actively engaged; prioritize promptly."],
], columns=["Warmth signal", "Points", "Use"])
st.dataframe(warmth_rules, width="stretch", hide_index=True)

st.markdown("#### Pre-Contact Checklist")
precontact = pd.DataFrame([
    ["1", "Identity", "Verify company, role, location, public professional contact route"],
    ["2", "Trigger", "Find one current, source-backed reason the conversation may be relevant"],
    ["3", "Relationship graph", "Check COIs, shared groups/events, prior relationships, and referral paths"],
    ["4", "Context", "Read company/about/news and identify one accurate observation"],
    ["5", "Value", "Choose one approved educational resource, question, event, or useful introduction"],
    ["6", "Channel", "Use the warmest legitimate channel: introduction > event follow-up > prior relationship > contextual direct outreach"],
    ["7", "First-touch brief", "Prepare a 30-second call opener plus short email/LinkedIn draft for human approval"],
    ["8", "Next action", "Pre-schedule the follow-up task so no prospect falls through the cracks"],
], columns=["Step", "Check", "Output"])
st.dataframe(precontact, width="stretch", hide_index=True)

st.subheader("Daily Hot List")
st.caption("Rank real records from connected public/approved feeds. Do not fabricate records just to fill the queue.")
columns = ["Prospect", "Type", "Area", "Opportunity score", "Warmth score", "Warmth", "Trigger", "Warm path", "Why now", "Conversation angle", "Last touch", "Next action", "Source"]
if "hot_list" not in st.session_state:
    st.session_state.hot_list = pd.DataFrame(columns=columns)
edited = st.data_editor(st.session_state.hot_list, num_rows="dynamic", width="stretch", hide_index=True, key="hot_list_editor")
if st.button("Save Hot List", type="primary"):
    st.session_state.hot_list = edited
    st.success("Hot list saved for this session. Persistent storage can be wired to PostgreSQL as the ingestion layer is activated.")

st.subheader("First-Touch Brief Builder")
left,right = st.columns(2)
with left:
    prospect_name = st.text_input("Prospect / company")
    role = st.text_input("Role")
    public_trigger = st.text_input("Verified public trigger")
    source = st.text_input("Trigger source / URL")
with right:
    warm_path = st.selectbox("Warmest available path", ["Direct introduction", "Event / shared organization", "Prior professional relationship", "Contextual direct outreach", "Cold - continue warming first"])
    coi_name = st.text_input("Potential introducer / shared connection")
    public_fact = st.text_input("One verified company-specific fact")
    value_item = st.text_input("Approved value item / useful reason to talk")

if st.button("Build First-Touch Brief"):
    if not prospect_name.strip():
        st.warning("Enter a prospect or company first.")
    else:
        st.markdown("#### Human-Review Brief")
        st.write(f"**Prospect:** {prospect_name} {('- ' + role) if role else ''}")
        st.write(f"**Warm path:** {warm_path}")
        if coi_name: st.write(f"**Introducer/shared connection:** {coi_name}")
        if public_trigger: st.write(f"**Why now:** {public_trigger}")
        if public_fact: st.write(f"**Relevant fact:** {public_fact}")
        if value_item: st.write(f"**Value before ask:** {value_item}")
        st.write("**Conversation objective:** earn a short discovery conversation, not make a product recommendation from public data.")
        st.write("**Suggested structure:** context → accurate observation → owner/executive question → useful next step → two specific meeting options.")
        st.caption("Draft actual external wording only after confirming the channel and content are permitted by NYL policy.")

st.subheader("Warm-Path Queue")
paths = pd.DataFrame(columns=["Prospect", "Potential introducer", "Shared organization/event", "Relationship strength", "Intro requested?", "Intro received?", "Next action", "Due date"])
st.data_editor(paths, num_rows="dynamic", width="stretch", hide_index=True, key="warm_paths")

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
st.caption(f"Monitoring configuration: {len(selected)} trigger categories in {territory}. Salesforce can be plugged into the relationship check later.")

st.subheader("Centers of Influence")
coi = pd.DataFrame(columns=["Name / Firm", "COI type", "Area", "Relationship strength", "Potential introductions", "Last touch", "Next action"])
st.data_editor(coi, num_rows="dynamic", width="stretch", hide_index=True, key="coi_editor")
st.caption("Prioritize reciprocal, compliant professional relationships. Never imply an introduction or shared relationship that does not exist.")

st.subheader("Prospect Radar")
st.write("Geographic clustering is ready for a future map layer. Use business/market-level coordinates and avoid exposing precise private-residence locations.")

st.subheader("Conversion Learning")
conversion = pd.DataFrame(columns=["Date", "Segment", "Source", "Warmth at first touch", "Touches", "Conversations", "Appointments", "Placed sales", "Referrals"])
st.data_editor(conversion, num_rows="dynamic", width="stretch", hide_index=True, key="conversion_editor")
st.caption("This lets the system learn whether introduced, event-connected, contextual, or cold first touches actually convert best for you.")

st.subheader("Future CRM / Salesforce Bridge")
st.success("Reserved flow: match/dedupe → existing relationship check → permitted policy/client context → warm-path/next-best-opportunity ranking → activity sync. No Salesforce credentials are required now.")
st.code("PUBLIC/APPROVED DATA → TRIGGER + RELATIONSHIP GRAPH → WARMTH SCORE → FIRST-TOUCH BRIEF → HUMAN OUTREACH → APPOINTMENT → [FUTURE NYL CRM/SALESFORCE] → OUTCOME → LEARNING", language="text")

st.caption(f"Radar configuration updated {date.today().isoformat()} • Minimum score {min_score} • Daily list {show_n}")
