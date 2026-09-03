from __future__ import annotations

from datetime import date

import pandas as pd
import streamlit as st

from core.rep_profile import REP_NAME, TERRITORY_LABEL, TERRITORY_ZIP
from core.prospecting import PUBLIC_SOURCE_PLAYBOOKS, allowed_signal_note, public_search_queries, rank_prospects
from data.prospects import (
    add_prospect,
    add_touchpoint,
    get_prospects,
    get_touchpoints,
    init_prospect_db,
    touchpoint_stats,
    update_prospect,
)

st.set_page_config(page_title=f"Prospecting | {REP_NAME}", page_icon="🧭", layout="wide")
init_prospect_db()

st.title("Prospecting & Pipeline")
st.caption(f"{REP_NAME} • {TERRITORY_LABEL} • isolated working pipeline")
st.info(allowed_signal_note())
st.warning("Research and pipeline preparation do not authorize outreach. Contact eligibility and product authority remain separate gates.")

prospects = get_prospects()

c1, c2, c3 = st.columns(3)
c1.metric("Pipeline records", len(prospects))
c2.metric("Territory center", TERRITORY_ZIP)
c3.metric("Radius", "20 miles")

st.subheader("Lead Scout — Public Sources")
territory = st.text_input("Territory / city / county / ZIP", value=f"Simi Valley, CA {TERRITORY_ZIP}")
segment = st.text_input("Target professional/business segment", value="business owners professionals executives")
st.dataframe(pd.DataFrame(PUBLIC_SOURCE_PLAYBOOKS), width="stretch", hide_index=True)
if territory.strip():
    for item in public_search_queries(territory, segment):
        st.link_button(item["label"], item["search_url"], width="stretch")

st.divider()
st.subheader("Add Prospect")
with st.form("paul_add_prospect"):
    name = st.text_input("Prospect / lead name")
    organization = st.text_input("Organization / business")
    market_segment = st.selectbox("Segment", ["Business owner", "Executive", "Professional", "Homeowner", "Center of influence", "Corporation", "Other"])
    source = st.selectbox("Lead source", [p["source"] for p in PUBLIC_SOURCE_PLAYBOOKS] + ["Salesforce", "Other"])
    source_detail = st.text_input("Public source detail / URL / referral source")
    next_action = st.text_input("Next action", value="Research / human review")
    notes = st.text_area("Notes — do not enter sensitive client data")
    save = st.form_submit_button("Add prospect")
    if save:
        if not name.strip():
            st.error("Enter a prospect/lead name.")
        else:
            add_prospect(
                prospect_name=name,
                organization=organization,
                market_segment=market_segment,
                source=source,
                source_detail=source_detail,
                stage="New",
                fit_score=3,
                warmth_score=2,
                urgency_score=2,
                source_quality=4,
                consent_status="Unknown",
                next_action=next_action,
                next_action_date=str(date.today()),
                notes=notes,
            )
            st.success("Prospect added to Paul's isolated pipeline.")
            st.rerun()

prospects = get_prospects()
ranked = rank_prospects(prospects)
st.subheader("Priority Queue")
if ranked:
    view = pd.DataFrame([{
        "Priority": p.get("priority_score", ""),
        "Name": p.get("prospect_name", ""),
        "Organization": p.get("organization", ""),
        "Stage": p.get("stage", ""),
        "Source": p.get("source", ""),
        "Next action": p.get("next_action", ""),
        "Due": p.get("next_action_date", ""),
    } for p in ranked[:25]])
    st.dataframe(view, width="stretch", hide_index=True)
else:
    st.info("No Paul-specific pipeline records yet.")

st.subheader("Touches & Replies")
stats = touchpoint_stats()
a, b, c = st.columns(3)
a.metric("Total touches", stats.get("total_touches", 0))
b.metric("Inbound replies", stats.get("inbound", 0))
c.metric("Follow-ups flagged", stats.get("follow_ups", 0))

st.divider()
st.caption("Paul's pipeline uses a separate tenant database and does not read Chris Haake's Central Florida prospect records.")
