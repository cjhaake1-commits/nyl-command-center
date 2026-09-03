from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st

from core.rep_profile import REP_NAME, TERRITORY_LABEL

st.set_page_config(page_title=f"Prospect Intelligence | {REP_NAME}", page_icon="🔎", layout="wide")
st.title("Prospect Intelligence")
st.caption(f"{REP_NAME} • {TERRITORY_LABEL} • isolated research database")

DATA_PATH = Path("data/paul_prospect_intelligence.json")
LANES = [
    "New Business / Key Person",
    "Capital Formation / Funding",
    "Established Business Triggers",
    "Professional Practices",
    "Next Generation / Early Wealth",
    "Centers of Influence",
    "Simi Valley / Ventura County Events",
]
PRODUCTS = [
    "Key-person life",
    "Disability / overhead protection",
    "Buy-sell / succession",
    "Executive benefits / retention",
    "Group life / disability",
    "Term life",
    "Permanent life / cash value",
    "Retirement-plan education",
    "Other — review authorization first",
]


def load_records() -> list[dict]:
    if not DATA_PATH.exists():
        return []
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []


def save_records(records: list[dict]) -> None:
    DATA_PATH.write_text(json.dumps(records, indent=2), encoding="utf-8")

records = load_records()
st.error("CONTACT GATE: HOLD — RESEARCH & QUALIFICATION ONLY until the applicable authorization and compliance gates are satisfied.")

c1, c2, c3 = st.columns(3)
c1.metric("Paul-specific prospects", len(records))
c2.metric("High opportunity", sum(1 for r in records if int(r.get("opportunity_score", 0) or 0) >= 85))
c3.metric("Contact eligible", sum(1 for r in records if bool(r.get("contact_eligible", False))))

t1, t2, t3 = st.tabs(["Master Database", "Register Lead", "Compliance / Product Gate"])
with t1:
    if records:
        st.dataframe(pd.DataFrame(records), width="stretch", hide_index=True)
    else:
        st.info("No Paul-specific prospect-intelligence records yet. Chris Haake's Florida intelligence database is not loaded in this tenant.")

with t2:
    with st.form("paul_register_prospect"):
        name = st.text_input("Person / decision maker")
        company = st.text_input("Company / organization")
        location = st.text_input("Location", value="Simi Valley, CA")
        lanes = st.multiselect("Intelligence lanes", LANES)
        source = st.text_input("Public source / URL")
        trigger = st.text_area("Why now / trigger evidence")
        opportunity = st.slider("Opportunity score", 0, 100, 50)
        products = st.multiselect("Potential planning / product fit", PRODUCTS)
        notes = st.text_area("Research notes")
        submitted = st.form_submit_button("Register research record")
        if submitted:
            if not (name.strip() or company.strip()) or not source.strip():
                st.warning("Add a person/company and a public source before saving.")
            else:
                records.append({
                    "name": name.strip(),
                    "company": company.strip(),
                    "location": location.strip(),
                    "lanes": lanes,
                    "source": source.strip(),
                    "source_date": date.today().isoformat(),
                    "trigger": trigger.strip(),
                    "opportunity_score": opportunity,
                    "product_fit": products,
                    "notes": notes.strip(),
                    "contact_status": "HOLD — RESEARCH ONLY",
                    "contact_eligible": False,
                })
                save_records(records)
                st.success("Saved to Paul's isolated intelligence file.")
                st.rerun()

with t3:
    st.warning("Potential fit does not mean Paul is authorized to offer or discuss every listed product. Use Make a Request to add verified product authority or change the matching logic.")
    st.dataframe(pd.DataFrame([
        ["Opportunity quality", "Research score only", "Never overrides compliance"],
        ["Contact eligibility", "Separate gate", "Requires channel/contact review"],
        ["Product authority", "Separate gate", "Requires verified license/appointment/firm authorization"],
        ["Custom scripts", "Draft/HOLD", "Use approved language/process before execution"],
    ], columns=["Control", "Default", "Rule"]), width="stretch", hide_index=True)
