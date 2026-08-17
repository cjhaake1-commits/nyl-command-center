from __future__ import annotations

import pandas as pd
import streamlit as st

st.title("Opportunity Radar")
st.caption("Turn prospect signals into prioritized next actions. Designed to complement the lead lists, prospect intelligence, marketing, and future CRM/Salesforce connection.")

st.subheader("Next-Best-Action Engine")
st.write("Score each prospect using fit + timing + relationship warmth + public trigger events + service breadth, then surface the highest-value action instead of simply showing another lead list.")

weights = pd.DataFrame([
    ["Service fit", 25, "How strongly the prospect matches one or more approved service conversations"],
    ["Timing / trigger", 20, "Public business or life-stage signal suggesting a conversation may be timely"],
    ["Relationship warmth", 20, "Referral, event interaction, prior touch, mutual connection, or inbound engagement"],
    ["Economic / business fit", 15, "Business scale or broad geographic/market indicators; avoid sensitive individual profiling"],
    ["Multi-service potential", 10, "Potential relevance across multiple planning conversations"],
    ["Data confidence", 10, "Freshness and reliability of public/licensed source data"],
], columns=["Factor", "Max points", "Meaning"])
st.dataframe(weights, use_container_width=True, hide_index=True)

st.subheader("Trigger Events to Watch")
triggers = pd.DataFrame([
    ["Business formation / expansion", "Business", "Owner protection, employee benefits, succession, retirement"],
    ["Hiring / headcount growth", "Business", "Benefits and business-owner planning"],
    ["Leadership / ownership change", "Business", "Succession and continuity conversations"],
    ["New commercial location", "Business", "Growth-stage planning review"],
    ["Public retirement-oriented event or inquiry", "Individual", "Retirement and protection review"],
    ["Home purchase / relocation signal from permissible public/licensed source", "Household", "Protection review; do not infer sensitive financial status"],
    ["Event attendance / QR scan / form response", "Warm lead", "Immediate personalized follow-up"],
    ["Referral introduction", "Warm lead", "Priority contact and referral-source acknowledgement"],
], columns=["Signal", "Lane", "Possible conversation"])
st.dataframe(triggers, use_container_width=True, hide_index=True)

st.subheader("Daily Priority Queue")
st.markdown("When the lead database is connected, this page should automatically produce: **Call Now**, **Research First**, **Send Value Touch**, **Invite to Event**, **Ask for Introduction**, **Nurture**, and **Do Not Contact / Suppressed** queues.")

st.subheader("Referral Flywheel")
st.write("Track centers of influence separately from prospects: CPAs, attorneys, real-estate professionals, mortgage professionals, business brokers, benefits professionals, bankers, association leaders, and community connectors. Rank them by relationship strength, introductions generated, opportunity quality, and reciprocal value.")

st.subheader("Pipeline Leak Detector")
st.write("Flag leads with no next action, overdue follow-ups, high-score prospects with too few touches, appointments without follow-up, stalled opportunities, and clients/prospects with potential multi-service conversations not yet reviewed.")

st.subheader("Pre-Meeting Brief")
st.write("Future one-click brief: public company/person context, prior touches, referral source, likely conversation areas, questions to ask, objections to prepare for, compliance reminders, and a blank notes area for facts learned directly from the prospect.")

st.subheader("Compliance & Data Hygiene")
st.info("Keep source URL/provider, collection date, consent/relationship status, suppression status, last verification date, and permitted-use notes with every record. Do not infer or append sensitive personal attributes from public data. Any future NYL/Salesforce integration should respect firm permissions, retention rules, and approved communications workflows.")
