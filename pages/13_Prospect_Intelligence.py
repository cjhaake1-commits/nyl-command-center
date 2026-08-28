from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st

st.title("Prospect Intelligence")
st.caption("Build the audience now. Activate it only after licensing, appointment, compliance, and approved-contact gates are satisfied.")

DATA_PATH = Path("data/prospect_intelligence.json")
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

LANES = [
    "New Business / Key Person",
    "Pre-Form-D / Capital Formation",
    "Form D / Private Placement",
    "Established Business Triggers",
    "Jewelry & Luxury",
    "Next Generation / Early Wealth",
    "Young Founders / Entrepreneurial Universities",
    "Orlando Events / Test Market",
]
PRODUCTS = [
    "Key-person life", "Disability / overhead protection", "Buy-sell / succession",
    "Executive benefits / retention", "Group life / disability", "Term life",
    "Permanent life / cash value", "Employer retirement-plan education",
    "IRA / Roth IRA", "Mutual funds / ETFs / brokerage", "529 / family planning",
]

def load_records():
    if not DATA_PATH.exists():
        return []
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_records(records):
    DATA_PATH.write_text(json.dumps(records, indent=2), encoding="utf-8")

records = load_records()

st.error("GLOBAL CONTACT GATE: HOLD — RESEARCH & QUALIFICATION ONLY. No email, call, text, social outreach, event solicitation, or in-person prospecting is authorized from this workspace yet.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Master prospects", len(records))
c2.metric("High key-person", sum(1 for r in records if int(r.get("key_person_score", 0)) >= 80))
c3.metric("Capital-raise signals", sum(1 for r in records if any(x in r.get("lanes", []) for x in LANES[1:3])))
c4.metric("Contact eligible", "0")

tabs = st.tabs(["Master Database", "Register Lead", "Intelligence Feeds", "Next Generation", "Events & Feedback", "Compliance Gate"])

with tabs[0]:
    st.subheader("Unified Prospect Database")
    st.write("One record can belong to multiple lanes. Opportunity measures relevance; Contact Eligibility is a separate hard gate.")
    if records:
        df = pd.DataFrame(records)
        preferred = ["name", "company", "location", "lanes", "opportunity_score", "key_person_score", "lead_temperature", "trigger", "contact_status", "source"]
        cols = [c for c in preferred if c in df.columns]
        st.dataframe(df[cols], use_container_width=True, hide_index=True)
    else:
        st.info("No registered prospects yet. Use Register Lead as research identifies qualified people and companies.")

with tabs[1]:
    st.subheader("Register / Score a Prospect")
    with st.form("register_prospect"):
        left, right = st.columns(2)
        with left:
            name = st.text_input("Person / founder / decision maker")
            company = st.text_input("Company / organization")
            location = st.text_input("Location")
            lanes = st.multiselect("Intelligence lanes", LANES)
            source = st.text_input("Source URL / provider / filing reference")
            source_date = st.date_input("Source date", value=date.today())
            trigger = st.text_area("Why now / trigger evidence")
        with right:
            opportunity_score = st.slider("Opportunity score", 0, 100, 50)
            key_person_score = st.slider("Key-person probability", 0, 100, 0)
            relationship_score = st.slider("Relationship potential", 0, 100, 50)
            lead_temperature = st.selectbox("Lead temperature", ["Cold Qualified", "Triggered", "Engaged", "Warm", "Active Opportunity", "Nurture / Watch"])
            products = st.multiselect("Potential product / education fit", PRODUCTS)
            evidence = st.text_area("Operating / fundraising / founder-dependency evidence")
        notes = st.text_area("Research notes / eventual contact-plan notes")
        submitted = st.form_submit_button("Register research record")
        if submitted:
            if not (company or name) or not source:
                st.warning("Add a person or company and a source/provenance reference before registering the record.")
            else:
                records.append({
                    "name": name, "company": company, "location": location, "lanes": lanes,
                    "source": source, "source_date": source_date.isoformat(), "trigger": trigger,
                    "opportunity_score": opportunity_score, "key_person_score": key_person_score,
                    "relationship_score": relationship_score, "lead_temperature": lead_temperature,
                    "product_fit": products, "evidence": evidence, "notes": notes,
                    "contact_status": "HOLD — RESEARCH ONLY", "contact_eligible": False,
                })
                save_records(records)
                st.success("Prospect registered under HOLD — RESEARCH ONLY.")
                st.rerun()

with tabs[2]:
    st.subheader("Eight Simultaneous Intelligence Feeds")
    feed_rows = [
        [LANES[0], "New incorporations + operating validation + founder dependency", "Key-person, disability, buy-sell"],
        [LANES[1], "Public fundraising language, 506(c), Reg CF/A, accelerators, demo days, pitch competitions", "Find founders before Form D"],
        [LANES[2], "SEC Form D / public private-placement signals", "Capital-at-risk + founder dependency"],
        [LANES[3], "Financing, M&A, expansion, hiring, leadership and succession", "Continuity / executive protection"],
        [LANES[4], "Jewelers, watch, luxury, wholesale/manufacturing", "Use operator-level industry knowledge"],
        [LANES[5], "Recent graduates / early-career professionals from permissible sources", "Start-early wealth education"],
        [LANES[6], "Babson prototype + founder-heavy universities, incubators and accelerators", "Young founder + capital formation"],
        [LANES[7], "Orlando young-professional/founder ecosystems and future approved events", "Live message testing + opt-in relationships"],
    ]
    st.dataframe(pd.DataFrame(feed_rows, columns=["Feed", "Signals", "Primary purpose"]), use_container_width=True, hide_index=True)
    st.markdown("**Research lifecycle:** Discover → Verify → Deduplicate → Enrich → Classify → Score → Product-fit → Compliance/Licensing Gate → Monitor → Rescore → Hold")

with tabs[3]:
    st.subheader("Next Generation / Early Wealth")
    st.markdown("**Core positioning:** Start small. Start automatically. Most importantly, start early.")
    age = st.slider("Illustration starting age", 18, 45, 22)
    monthly = st.number_input("Illustrative monthly contribution", min_value=0.0, value=250.0, step=25.0)
    rate = st.slider("Hypothetical annual return (%)", 0.0, 12.0, 7.0, 0.5) / 100
    years = max(0, 65 - age)
    months = years * 12
    monthly_rate = rate / 12
    fv = monthly * months if monthly_rate == 0 else monthly * (((1 + monthly_rate) ** months - 1) / monthly_rate)
    contributed = monthly * months
    a, b, c = st.columns(3)
    a.metric("Contributed", f"${contributed:,.0f}")
    b.metric("Hypothetical value at 65", f"${fv:,.0f}")
    c.metric("Hypothetical growth", f"${max(0, fv-contributed):,.0f}")
    st.caption("Educational hypothetical only; not a prediction or guarantee. Actual returns, taxes, fees, plan rules, suitability and product minimums vary.")
    st.markdown("**Financial ladder:** employer-plan/match education → emergency liquidity → automatic investing → appropriate protection → permanent protection/cash-value education when suitable → advanced accumulation only when appropriate.")
    st.markdown("**Priority cohorts:** recent graduates, young physicians, attorneys, engineers, technology/finance professionals, successful salespeople, new managers, entrepreneurs, and founder-heavy university ecosystems such as Babson.")

with tabs[4]:
    st.subheader("Orlando Event Laboratory")
    st.write("Prepare future NYL-approved educational/social formats and record first-hand feedback before scaling colder national approaches.")
    concepts = pd.DataFrame([
        ["Future You Happy Hour", "Young professionals", "Time value of money, employer benefits, automation"],
        ["Founder Risk Happy Hour", "Founders", "Key-person dependency, disability, continuity, buy-sell"],
        ["First $100K Club", "Early wealth", "Milestone-based investing education"],
    ], columns=["Concept", "Audience", "Learning theme"])
    st.dataframe(concepts, use_container_width=True, hide_index=True)
    st.markdown("Track: registrations, attendance, source, questions, objections, concepts that resonate, calculator completions, voluntary opt-ins, requested follow-ups, appointments and eventual outcomes. Event materials remain draft-only until required NYL approval is documented.")

with tabs[5]:
    st.subheader("Licensing & Contact Eligibility")
    st.warning("Opportunity score never overrides compliance. A 100/100 prospect remains HOLD until every applicable gate is satisfied.")
    gates = pd.DataFrame([
        ["Insurance license", "Not unlocked here", "Required jurisdiction/product authority verified"],
        ["Carrier appointment", "Not unlocked here", "NYL appointment/authority verified"],
        ["Securities registration", "Not unlocked here", "Required registration/firm authorization verified"],
        ["Approved material", "Not unlocked here", "NYL-approved template/script/event material"],
        ["Channel compliance", "Not unlocked here", "TCPA/DNC/CAN-SPAM/state/firm rules satisfied"],
        ["Suppression / opt-out", "Required", "No conflict with DNC, suppression or prior opt-out"],
    ], columns=["Gate", "Current state", "Unlock condition"])
    st.dataframe(gates, use_container_width=True, hide_index=True)
    st.info("The database may research and prepare future contact protocols, but it does not execute outreach.")
