from __future__ import annotations

from datetime import datetime, timezone
import json

import streamlit as st

from core.rep_profile import REP_NAME, TERRITORY_CITY, TERRITORY_LABEL, TERRITORY_RADIUS_MILES, TERRITORY_ZIP

st.set_page_config(page_title=f"Make a Request | {REP_NAME}", page_icon="📝", layout="wide")
st.title("Make a Request")
st.caption("Ask a question, request a new lead focus, or tailor the Command Center to how you want to work.")

st.info(
    "Requests are planning inputs only. They do not authorize prospect contact, solicitation, product claims, or other outreach. "
    "Compliance and contact-eligibility rules remain separate from opportunity quality."
)

request_types = [
    "Ask a question",
    "Change prospecting focus",
    "Request a lead list",
    "Change territory / radius",
    "Add an industry or profession",
    "Adjust lead scoring priorities",
    "Tailor call / email scripts",
    "Add or change Salesforce fields",
    "Add a workflow or dashboard feature",
    "Report a problem",
    "Other",
]

with st.form("paul_request_form", clear_on_submit=False):
    c1, c2 = st.columns(2)
    with c1:
        request_type = st.selectbox("Request type", request_types)
        priority = st.selectbox("Priority", ["Normal", "High", "Urgent"])
    with c2:
        lead_group = st.selectbox(
            "Applies to",
            ["Both individuals and businesses", "Individual Consumers", "Small Business Consumers", "App / workflow only"],
        )
        requested_radius = st.number_input(
            "Desired radius (miles)",
            min_value=1,
            max_value=100,
            value=int(TERRITORY_RADIUS_MILES),
            step=1,
        )

    question = st.text_area(
        "Question or request",
        placeholder="Example: Find more CPA and law-firm owners within 15 miles, or explain why a specific person was selected.",
        height=150,
    )
    desired_outcome = st.text_area(
        "What would make this useful?",
        placeholder="Describe the result you want: a new lead batch, a new filter, different scoring, a script change, etc.",
        height=110,
    )
    notes = st.text_area("Anything else I should know?", height=90)

    submitted = st.form_submit_button("Create Request", type="primary", use_container_width=True)

if submitted:
    if not question.strip():
        st.error("Please enter a question or request.")
    else:
        request = {
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "rep": REP_NAME,
            "request_type": request_type,
            "priority": priority,
            "applies_to": lead_group,
            "territory_zip": TERRITORY_ZIP,
            "territory_city": TERRITORY_CITY,
            "territory_label": TERRITORY_LABEL,
            "requested_radius_miles": int(requested_radius),
            "question_or_request": question.strip(),
            "desired_outcome": desired_outcome.strip(),
            "notes": notes.strip(),
            "status": "NEW",
        }
        st.session_state.setdefault("paul_requests", []).append(request)
        st.success("Request created. You can download or copy it below and send it for implementation/research.")
        st.json(request)
        payload = json.dumps(request, indent=2)
        st.download_button(
            "Download Request JSON",
            payload,
            file_name=f"paul_deck_request_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True,
        )

st.divider()
st.subheader("Requests created this session")
requests = st.session_state.get("paul_requests", [])
if not requests:
    st.caption("No requests created in this session yet.")
else:
    for i, item in enumerate(reversed(requests), start=1):
        with st.expander(f"{i}. {item['request_type']} • {item['priority']} • {item['status']}"):
            st.write(item["question_or_request"])
            if item.get("desired_outcome"):
                st.caption(f"Desired outcome: {item['desired_outcome']}")
            st.caption(f"Territory request: {item['requested_radius_miles']} miles around {item['territory_zip']}")

st.caption("The default territory remains 93065 with a 20-mile radius unless a reviewed configuration change is actually applied.")
