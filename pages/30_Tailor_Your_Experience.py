from __future__ import annotations

import json
import pandas as pd
import streamlit as st

from core.rep_profile import PROFILE, REP_NAME, TERRITORY_CITY, TERRITORY_LABEL, TERRITORY_RADIUS_MILES
from data.community_hub import init_community_tables, list_requests, submit_request

st.set_page_config(page_title=f"Tailor Your Experience | {REP_NAME}", page_icon="🛠️", layout="wide")
init_community_tables()
REP_EMAIL = PROFILE.get("email") or f"{REP_NAME} profile pending"

st.title("Tailor Your Experience")
st.caption(f"Your direct request desk • {REP_NAME} Command Center")
st.success(
    "Request prospect lists, event research, territory or industry changes, scripts, or app improvements here. "
    "Submit requests directly from your Command Center—no need to route them through your manager."
)
st.info(
    "Requests are saved to your request queue and can be downloaded below. Submitting a request does not automatically contact prospects "
    "or change NYL-approved materials."
)

request_types = [
    "Request a prospect list", "Find and add events", "Add an industry or community",
    "Change territory or filters", "Tailor a script or conversation guide",
    "Change app layout or workflow", "Ask a question", "Report an issue", "Other",
]
focus_options = ["Veterinary clinics", "Ocala equestrian community", "Both", "Central Florida businesses", "Other"]
with st.form("tailor_experience_request", clear_on_submit=False):
    c1, c2 = st.columns(2)
    with c1:
        request_type = st.selectbox("What do you want help with?", request_types)
        focus = st.selectbox("Prospecting focus", focus_options)
        priority = st.selectbox("Priority", ["Normal", "High", "Urgent"])
    with c2:
        territory = st.text_input("Territory", value=f"{TERRITORY_LABEL} • {TERRITORY_CITY}")
        radius = st.number_input("Desired radius (miles)", min_value=1, max_value=250, value=int(TERRITORY_RADIUS_MILES), step=5)
        date_range = st.text_input("Event date range (if relevant)", placeholder="e.g., next 60 days")
    request_text = st.text_area(
        "Describe the list, research, or change you want *",
        placeholder="Include audience, geography, date range, useful sources, and the deliverable you want.",
        height=160,
    )
    desired_result = st.text_area(
        "What would make the result useful?",
        placeholder="Example: 20 verified clinics, public business contacts, relationship notes, and an exportable list.",
        height=100,
    )
    submitted = st.form_submit_button("Submit my request", type="primary", use_container_width=True)

if submitted:
    if not request_text.strip():
        st.error("Describe what you want researched or changed.")
    else:
        full_request = (
            f"Priority: {priority}\nRequested radius: {int(radius)} miles\n"
            f"Event date range: {date_range.strip() or 'Not specified'}\n"
            f"Request: {request_text.strip()}\nDesired result: {desired_result.strip() or 'Not specified'}"
        )
        submit_request(REP_EMAIL, request_type, focus, territory.strip(), full_request)
        st.success("Your request is in the request queue.")
        st.rerun()

st.divider()
st.subheader("Your request history")
all_requests = list_requests(limit=500)
mine = [r for r in all_requests if str(r.get("rep_email", "")).casefold() == REP_EMAIL.casefold()]
if mine:
    df = pd.DataFrame(mine)
    st.dataframe(df[["created_at", "request_type", "focus", "territory", "request_text", "status"]], width="stretch", hide_index=True)
    st.download_button(
        "Download my requests",
        json.dumps(mine, indent=2, ensure_ascii=False),
        file_name=f"{REP_NAME.lower().replace(' ', '_')}_experience_requests.json",
        mime="application/json",
        use_container_width=True,
    )
else:
    st.caption("Your submitted requests will appear here.")
st.caption(f"Request owner: {REP_NAME} • Territory defaults can be changed in each request.")
