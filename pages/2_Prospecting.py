from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import streamlit as st

from core.prospecting import (
    PUBLIC_SOURCE_PLAYBOOKS,
    allowed_signal_note,
    lead_gap,
    public_search_queries,
    rank_prospects,
)
from data.db import totals
from data.prospects import add_prospect, get_prospects, init_prospect_db, prospect_counts, update_prospect

st.set_page_config(page_title="NYL Prospecting", page_icon="🧭", layout="wide")
init_prospect_db()

st.title("Prospecting & Pipeline")
st.caption("Find public-facing lead opportunities, maintain a lightweight prospect pipeline, and decide who to contact next.")
st.info(allowed_signal_note())

activity = totals()
counts = prospect_counts()

st.subheader("Lead Inventory")
new_name_share = st.slider("Share of daily outreach that should come from new names", 10, 80, 35, step=5) / 100
coverage_days = st.slider("Lead inventory coverage", 2, 15, 5)
# Use recent observed outreach when available; otherwise use the War Room's current default-scale target.
recent_outreach = max(1, int(activity.get("outreach_attempts", 0) or 0))
planning_outreach = st.number_input("Planned outreach attempts per day", min_value=1, value=max(67, recent_outreach), step=1)
gap = lead_gap(int(counts.get("active", 0)), planning_outreach, new_name_share, coverage_days)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Active prospects", gap["active_prospects"])
c2.metric("New names/day", gap["daily_new_names"])
c3.metric(f"{gap['coverage_days']}-day inventory target", gap["pipeline_target"])
c4.metric("Lead gap", gap["gap"])

if gap["gap"] > 0:
    st.warning(f"Build at least {gap['gap']} additional qualified names to reach your current lead-inventory target.")
else:
    st.success("Your active lead inventory currently covers the prospecting target you set.")

st.subheader("Lead Scout — Public Sources")
territory = st.text_input("Territory / city / county / ZIP", placeholder="Example: Buffalo NY or Erie County NY")
segment = st.text_input("Target professional/business segment", value="business owners professionals executives")

playbook_df = pd.DataFrame(PUBLIC_SOURCE_PLAYBOOKS)
st.dataframe(playbook_df, width="stretch", hide_index=True)

if territory.strip():
    st.markdown("#### Research Launchpad")
    st.caption("These links open public web searches for manual review. They do not scrape, auto-enrich, or auto-contact anyone.")
    for item in public_search_queries(territory, segment):
        st.link_button(item["label"], item["search_url"], width="stretch")

st.markdown("#### Sources to prioritize")
st.markdown(
    "- **Corporations/business owners:** company websites, chambers, trade associations, Secretary of State filings, local business journals, expansion/hiring announcements, public commercial-property records.\n"
    "- **Professionals/individuals:** public professional profiles, public promotions/job changes, property purchase/public-record signals, referrals, public community/professional events.\n"
    "- **Territory planning:** Census/ACS and government statistics for aggregate ZIP/county/city market characteristics — not sensitive individual profiling."
)

st.divider()
st.subheader("Add Prospect")
with st.form("add_prospect"):
    name = st.text_input("Prospect / lead name")
    organization = st.text_input("Organization / business")
    market_segment = st.selectbox(
        "Segment",
        ["Broad market", "Business owner", "Executive", "Professional", "Homeowner", "Real-estate investor", "Center of influence", "Corporation"],
    )
    source = st.selectbox("Lead source", [p["source"] for p in PUBLIC_SOURCE_PLAYBOOKS] + ["Salesforce", "Other"])
    source_detail = st.text_input("Public source detail / URL / referral source")
    stage = st.selectbox("Stage", ["New", "Attempting contact", "Connected", "Needs identified", "Appointment set", "Follow-up", "Won", "Lost"])

    s1, s2, s3, s4 = st.columns(4)
    fit = s1.slider("Fit", 1, 5, 3)
    warmth = s2.slider("Warmth", 1, 5, 3)
    urgency = s3.slider("Timing", 1, 5, 3)
    source_quality = s4.slider("Source quality", 1, 5, 3)

    consent = st.selectbox("Contact status", ["Unknown", "Permission / opt-in", "Existing relationship", "Do not contact"])
    next_action = st.text_input("Next action", value="Research / human review")
    next_action_date = st.date_input("Next action date", value=date.today())
    salesforce_id = st.text_input("Salesforce record ID (optional / future sync)")
    notes = st.text_area("Notes — do not enter SSNs, medical data, account numbers, or other sensitive client data")
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
                stage=stage,
                fit_score=fit,
                warmth_score=warmth,
                urgency_score=urgency,
                source_quality=source_quality,
                consent_status=consent,
                next_action=next_action,
                next_action_date=str(next_action_date),
                salesforce_record_id=salesforce_id,
                crm_source="Salesforce" if salesforce_id else "Command Center",
                do_not_contact=consent == "Do not contact",
                notes=notes,
            )
            st.success("Prospect added.")
            st.rerun()

prospects = get_prospects()
ranked = rank_prospects(prospects)

st.divider()
st.subheader("Who Do I Contact Next?")
if ranked:
    top = ranked[:10]
    priority_df = pd.DataFrame([
        {
            "Priority": p["priority_score"],
            "Name": p["prospect_name"],
            "Organization": p.get("organization", ""),
            "Stage": p.get("stage", ""),
            "Source": p.get("source", ""),
            "Next action": p.get("next_action", ""),
            "Due": p.get("next_action_date", ""),
            "CRM": p.get("crm_source", ""),
        }
        for p in top
    ])
    st.dataframe(priority_df, width="stretch", hide_index=True)
    first = top[0]
    st.success(
        f"Next best action: {first['prospect_name']} — {first.get('next_action') or 'human review / follow-up'} "
        f"(priority {first['priority_score']})."
    )
else:
    st.info("Add prospects to activate the priority engine.")

st.subheader("Update Prospect")
if prospects:
    labels = {f"#{p['id']} — {p['prospect_name']} ({p['stage']})": p for p in prospects}
    selected_label = st.selectbox("Select prospect", list(labels.keys()))
    selected = labels[selected_label]
    with st.form("update_prospect"):
        stage_u = st.selectbox(
            "Stage",
            ["New", "Attempting contact", "Connected", "Needs identified", "Appointment set", "Follow-up", "Won", "Lost"],
            index=["New", "Attempting contact", "Connected", "Needs identified", "Appointment set", "Follow-up", "Won", "Lost"].index(selected["stage"]),
        )
        next_action_u = st.text_input("Next action", value=selected.get("next_action") or "")
        due_default = date.today()
        try:
            if selected.get("next_action_date"):
                due_default = date.fromisoformat(str(selected["next_action_date"])[:10])
        except ValueError:
            pass
        next_date_u = st.date_input("Next action date", value=due_default)
        last_contact_u = st.date_input("Last contact date", value=date.today())
        consent_u = st.selectbox(
            "Contact status",
            ["Unknown", "Permission / opt-in", "Existing relationship", "Do not contact"],
            index=["Unknown", "Permission / opt-in", "Existing relationship", "Do not contact"].index(selected.get("consent_status") or "Unknown"),
        )
        dnc_u = st.checkbox("Do not contact", value=bool(selected.get("do_not_contact")))
        notes_u = st.text_area("Notes", value=selected.get("notes") or "")
        update = st.form_submit_button("Save update")
        if update:
            update_prospect(
                selected["id"],
                stage=stage_u,
                next_action=next_action_u,
                next_action_date=str(next_date_u),
                last_contact_date=str(last_contact_u),
                consent_status=consent_u,
                do_not_contact=dnc_u or consent_u == "Do not contact",
                notes=notes_u,
            )
            st.success("Prospect updated.")
            st.rerun()

st.divider()
st.subheader("Salesforce Readiness")
st.info(
    "The pipeline is Salesforce-ready: each prospect can carry a Salesforce record ID and CRM source. "
    "When NYL authorizes Salesforce OAuth/API access, the intended architecture is Salesforce as the official system of record, "
    "with the Command Center reading approved fields for prioritization and optionally syncing permitted tasks/statuses back."
)

st.caption(
    "Compliance boundary: public availability does not automatically mean unrestricted solicitation. "
    "Before outreach, follow NYL-approved workflows, applicable do-not-call/consent rules, platform terms, and firm communications policies."
)
