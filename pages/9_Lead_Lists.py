from __future__ import annotations

from datetime import datetime
from io import BytesIO
import pandas as pd
import streamlit as st

from data.public_leads import PUBLIC_LEADS
from data.salesforce_lead_inventory import get_salesforce_lead_inventory

st.set_page_config(page_title="Lead Lists", page_icon="📋", layout="wide")
st.title("Lead Lists + Opportunity Match")
st.caption("Canonical delivered Salesforce inventory plus verified public-source prospecting records, with multi-service opportunity matching, ranking, provenance, and export tools.")

st.info("A lead can match multiple planning categories. Matches are prospecting hypotheses based on public business/professional signals—not product recommendations or proof of need. Confirm needs through approved fact-finding and only discuss services you are licensed/authorized to offer.")

SERVICE_CATALOG = [
    "Personal life protection", "Business-owner life protection", "Key-person protection",
    "Buy-sell / succession planning", "Business-owner retirement planning", "Retirement income / annuity conversation",
    "Executive benefits", "Employee life/disability benefits", "Disability planning", "Long-term care planning",
    "Estate / legacy planning coordination", "Investment / advisory conversation", "COI / referral relationship"
]

LEAD_COLUMNS = [
    "Lead type", "Name", "Company", "Role", "Industry", "Area", "Business age years", "Employees",
    "Business email", "Business phone", "Opportunity score", "Warmth score", "Warmth", "Trigger", "Warm path", "Why now",
    "Service matches", "Primary opportunity", "Opportunity count", "Source URL", "Verified date", "Next action", "Status"
]


def service_matches(row: pd.Series) -> list[str]:
    lead_type = str(row.get("Lead type", "")).lower()
    role = str(row.get("Role", "")).lower()
    industry = str(row.get("Industry", "")).lower()
    trigger = str(row.get("Trigger", "")).lower()
    why = str(row.get("Why now", "")).lower()
    text = " ".join([role, industry, trigger, why])
    try: employees = int(float(row.get("Employees", 0) or 0))
    except (ValueError, TypeError): employees = 0
    try: age = float(row.get("Business age years", 99) or 99)
    except (ValueError, TypeError): age = 99
    matches = []
    owner = any(k in role for k in ["owner", "founder", "partner", "president", "ceo", "principal"])
    executive = owner or any(k in role for k in ["executive", "chief", "vp", "vice president", "director"])
    professional = any(k in text for k in ["physician", "medical", "dental", "veterinary", "attorney", "law", "cpa", "accounting", "architect", "engineer", "consulting"])
    coi = any(k in text for k in ["cpa", "accounting", "attorney", "law", "bank", "commercial real estate", "realtor", "real estate", "mortgage", "title", "benefits", "local media", "publishing"])
    retirement_signal = any(k in text for k in ["retirement", "succession", "transition", "exit", "estate", "legacy"])
    growth = any(k in text for k in ["new business", "new registration", "hiring", "growth", "expansion", "new location", "acquisition", "opening", "contract"])

    if "business" in lead_type or owner or executive:
        matches.append("Business-owner life protection" if owner else "Personal life protection")
    else:
        matches.append("Personal life protection")
    if owner:
        matches += ["Business-owner retirement planning", "Disability planning"]
    if owner and ("partner" in role or any(k in text for k in ["partner", "multi-owner", "succession"])):
        matches.append("Buy-sell / succession planning")
    if owner or executive:
        matches.append("Key-person protection")
    if employees >= 10:
        matches.append("Employee life/disability benefits")
    if employees >= 10 and (executive or employees >= 25):
        matches.append("Executive benefits")
    if retirement_signal:
        matches += ["Retirement income / annuity conversation", "Estate / legacy planning coordination"]
    if professional or owner:
        matches.append("Estate / legacy planning coordination")
    if any(k in text for k in ["retirement", "wealth", "investment", "executive", "owner", "founder", "partner"]):
        matches.append("Investment / advisory conversation")
    if any(k in text for k in ["long-term care", "ltc", "retirement"]):
        matches.append("Long-term care planning")
    if coi or "coi" in lead_type:
        matches.append("COI / referral relationship")
    if age <= 10 and owner and growth:
        matches += ["Key-person protection", "Business-owner retirement planning"]
    return list(dict.fromkeys(matches))


def enrich_matches(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if out.empty:
        return out
    matches = out.apply(service_matches, axis=1)
    out["Service matches"] = matches.apply(lambda x: " | ".join(x))
    out["Opportunity count"] = matches.apply(len)
    out["Primary opportunity"] = matches.apply(lambda x: x[0] if x else "Human review")
    return out


def build_seed() -> pd.DataFrame:
    delivered = get_salesforce_lead_inventory().copy()
    public = pd.DataFrame(PUBLIC_LEADS)
    for frame in (delivered, public):
        for col in LEAD_COLUMNS:
            if col not in frame.columns:
                frame[col] = ""
    combined = pd.concat([delivered[LEAD_COLUMNS], public[LEAD_COLUMNS]], ignore_index=True)
    combined["_dedupe_key"] = (
        combined["Name"].astype(str).str.strip().str.lower()
        + "|"
        + combined["Company"].astype(str).str.strip().str.lower()
    )
    combined = combined.drop_duplicates("_dedupe_key", keep="first").drop(columns=["_dedupe_key"])
    return enrich_matches(combined.reset_index(drop=True))

seeded = build_seed()
seed_version = "salesforce-188-plus-public-v1"
if st.session_state.get("lead_list_seed_version") != seed_version:
    st.session_state.lead_list_master = seeded
    st.session_state.lead_list_seed_version = seed_version
elif "lead_list_master" not in st.session_state:
    st.session_state.lead_list_master = seeded

with st.sidebar:
    st.header("Lead List Filters")
    lead_type = st.multiselect("Lead type", ["Business", "Individual / professional", "COI"], default=["Business", "Individual / professional", "COI"])
    service_filter = st.multiselect("Opportunity / service match", SERVICE_CATALOG)
    min_matches = st.slider("Minimum matched opportunities", 0, 8, 0)
    min_opportunity = st.slider("Minimum opportunity score", 0, 100, 0)
    min_warmth = st.slider("Minimum warmth score", 0, 100, 0)
    search_text = st.text_input("Search name / company / industry / area")

st.subheader("Master Lead List")
individual_count = int((seeded["Lead type"] == "Individual / professional").sum())
business_count = int((seeded["Lead type"] == "Business").sum())
st.caption(f"Synced delivered inventory: 108 individuals + 80 businesses. Existing verified public-source leads are added only when name + company is not already present. Current deduplicated seed: {len(seeded)} leads.")
master = st.data_editor(st.session_state.lead_list_master, num_rows="dynamic", width="stretch", hide_index=True, key="master_lead_editor")
master = enrich_matches(master)
if st.button("Save + Recalculate Opportunity Matches", type="primary"):
    st.session_state.lead_list_master = master
    st.success("Lead list saved and every record was re-evaluated across all opportunity categories.")

filtered = master.copy()
if not filtered.empty:
    if lead_type:
        filtered = filtered[filtered["Lead type"].isin(lead_type)]
    for col, threshold in [("Opportunity score", min_opportunity), ("Warmth score", min_warmth), ("Opportunity count", min_matches)]:
        vals = pd.to_numeric(filtered.get(col, 0), errors="coerce").fillna(0)
        filtered = filtered[vals >= threshold]
    if service_filter:
        filtered = filtered[filtered["Service matches"].fillna("").apply(lambda x: any(s in x for s in service_filter))]
    if search_text.strip():
        q = search_text.strip().lower()
        searchable = filtered.astype(str).apply(lambda col: col.str.lower())
        filtered = filtered[searchable.apply(lambda row: row.str.contains(q, regex=False).any(), axis=1)]

st.subheader("Filtered / Exportable Leads")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Leads", len(filtered))
m2.metric("Multi-opportunity leads", int((pd.to_numeric(filtered.get("Opportunity count", 0), errors="coerce").fillna(0) >= 2).sum()) if not filtered.empty else 0)
m3.metric("Business", int((filtered.get("Lead type", pd.Series(dtype=str)) == "Business").sum()) if not filtered.empty else 0)
m4.metric("Individuals", int((filtered.get("Lead type", pd.Series(dtype=str)) == "Individual / professional").sum()) if not filtered.empty else 0)
st.dataframe(filtered, width="stretch", hide_index=True)

st.subheader("Opportunity Coverage")
if not filtered.empty:
    counts = []
    for service in SERVICE_CATALOG:
        n = int(filtered["Service matches"].fillna("").str.contains(service, regex=False).sum())
        if n:
            counts.append({"Opportunity category": service, "Matched leads": n})
    st.dataframe(pd.DataFrame(counts).sort_values("Matched leads", ascending=False) if counts else pd.DataFrame(columns=["Opportunity category", "Matched leads"]), width="stretch", hide_index=True)


def excel_bytes(df: pd.DataFrame) -> bytes:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Leads")
        ws = writer.book["Leads"]
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for cells in ws.columns:
            max_len = max((len(str(c.value)) if c.value is not None else 0) for c in cells)
            ws.column_dimensions[cells[0].column_letter].width = min(max(max_len + 2, 12), 50)
    return output.getvalue()


def pdf_bytes(df: pd.DataFrame) -> bytes:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import landscape, letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=landscape(letter), leftMargin=.2*inch, rightMargin=.2*inch, topMargin=.25*inch, bottomMargin=.25*inch)
    styles = getSampleStyleSheet()
    story = [Paragraph("NYL Command Center - Opportunity-Matched Lead List", styles["Title"]), Paragraph(f"Exported {datetime.now().strftime('%Y-%m-%d %H:%M')} | {len(df)} leads", styles["Normal"]), Spacer(1, 8)]
    preferred = ["Lead type", "Name", "Company", "Role", "Industry", "Area", "Business email", "Business phone", "Opportunity score", "Warmth score", "Primary opportunity", "Opportunity count", "Service matches", "Trigger", "Next action"]
    cols = [c for c in preferred if c in df.columns]
    printable = df[cols].fillna("").astype(str) if cols else df.fillna("").astype(str)
    data = [list(printable.columns)] + printable.values.tolist()
    table = Table(data, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 5), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), .25, colors.grey), ("LEFTPADDING", (0, 0), (-1, -1), 2), ("RIGHTPADDING", (0, 0), (-1, -1), 2)]))
    story.append(table)
    doc.build(story)
    return output.getvalue()

st.markdown("#### Export")
if filtered.empty:
    st.warning("No leads match the current filters.")
else:
    e1, e2 = st.columns(2)
    with e1:
        st.download_button("⬇️ Export Lead List to Excel", excel_bytes(filtered), f"nyl_leads_{datetime.now().strftime('%Y%m%d')}.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)
    with e2:
        st.download_button("⬇️ Export Lead List to PDF", pdf_bytes(filtered), f"nyl_leads_{datetime.now().strftime('%Y%m%d')}.pdf", "application/pdf", use_container_width=True)

st.divider()
st.caption("Opportunity matching is intentionally many-to-many: one lead may map to several planning conversations. Actual recommendations require approved discovery, licensing/registration where applicable, suitability, and NYL compliance.")