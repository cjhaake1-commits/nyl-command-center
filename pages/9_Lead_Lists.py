from __future__ import annotations

from datetime import datetime
from io import BytesIO

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Lead Lists", page_icon="📋", layout="wide")
st.title("Lead Lists")
st.caption("Your independent public-source prospecting lane: searchable, ranked business and professional leads with source provenance and export tools.")

st.info("Only use lawful public/business contact information and approved sources. Keep source URLs and verification dates. Suppress opt-outs/DNC/wrong-person records. NYL CRM/Salesforce can be cross-referenced later when authorized.")

LEAD_COLUMNS = [
    "Lead type", "Name", "Company", "Role", "Industry", "Area",
    "Business email", "Business phone", "Opportunity score", "Warmth score",
    "Warmth", "Trigger", "Warm path", "Why now", "Source URL",
    "Verified date", "Next action", "Status"
]

if "lead_list_master" not in st.session_state:
    st.session_state.lead_list_master = pd.DataFrame(columns=LEAD_COLUMNS)

with st.sidebar:
    st.header("Lead List Filters")
    lead_type = st.multiselect("Lead type", ["Business", "Individual / professional", "COI"], default=["Business", "Individual / professional", "COI"])
    min_opportunity = st.slider("Minimum opportunity score", 0, 100, 0)
    min_warmth = st.slider("Minimum warmth score", 0, 100, 0)
    search_text = st.text_input("Search name / company / industry / area")

st.subheader("Master Lead List")
st.caption("Real ingested leads will appear here. You can also add or correct records manually while public-data connectors are being activated.")

master = st.data_editor(
    st.session_state.lead_list_master,
    num_rows="dynamic",
    width="stretch",
    hide_index=True,
    key="master_lead_editor",
)

if st.button("Save Lead List", type="primary"):
    st.session_state.lead_list_master = master
    st.success("Lead list saved for this session.")

filtered = master.copy()
if not filtered.empty:
    if "Lead type" in filtered.columns and lead_type:
        filtered = filtered[filtered["Lead type"].isin(lead_type)]
    for col, threshold in [("Opportunity score", min_opportunity), ("Warmth score", min_warmth)]:
        if col in filtered.columns:
            vals = pd.to_numeric(filtered[col], errors="coerce").fillna(0)
            filtered = filtered[vals >= threshold]
    if search_text.strip():
        q = search_text.strip().lower()
        searchable = filtered.astype(str).apply(lambda col: col.str.lower())
        mask = searchable.apply(lambda row: row.str.contains(q, regex=False).any(), axis=1)
        filtered = filtered[mask]

st.subheader("Filtered / Exportable Leads")
m1,m2,m3,m4 = st.columns(4)
m1.metric("Leads", len(filtered))
m2.metric("Business", int((filtered.get("Lead type", pd.Series(dtype=str)) == "Business").sum()) if not filtered.empty else 0)
m3.metric("Individuals / professionals", int((filtered.get("Lead type", pd.Series(dtype=str)) == "Individual / professional").sum()) if not filtered.empty else 0)
m4.metric("COIs", int((filtered.get("Lead type", pd.Series(dtype=str)) == "COI").sum()) if not filtered.empty else 0)

st.dataframe(filtered, width="stretch", hide_index=True)


def excel_bytes(df: pd.DataFrame) -> bytes:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Leads")
        ws = writer.book["Leads"]
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for column_cells in ws.columns:
            max_len = max((len(str(cell.value)) if cell.value is not None else 0) for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = min(max(max_len + 2, 12), 45)
    return output.getvalue()


def pdf_bytes(df: pd.DataFrame) -> bytes:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import landscape, letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=landscape(letter), leftMargin=0.25*inch, rightMargin=0.25*inch, topMargin=0.3*inch, bottomMargin=0.3*inch)
    styles = getSampleStyleSheet()
    story = [Paragraph("NYL Command Center - Lead List", styles["Title"]), Paragraph(f"Exported {datetime.now().strftime('%Y-%m-%d %H:%M')} | {len(df)} leads", styles["Normal"]), Spacer(1, 8)]
    preferred = ["Lead type", "Name", "Company", "Role", "Industry", "Area", "Business email", "Business phone", "Opportunity score", "Warmth score", "Trigger", "Next action"]
    cols = [c for c in preferred if c in df.columns]
    printable = df[cols].fillna("").astype(str) if cols else df.fillna("").astype(str)
    data = [list(printable.columns)] + printable.values.tolist()
    table = Table(data, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 6),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.grey),
        ("LEFTPADDING", (0,0), (-1,-1), 2),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    story.append(table)
    doc.build(story)
    return output.getvalue()

st.markdown("#### Export")
if filtered.empty:
    st.warning("There are no filtered leads to export yet. Once the ingestion feeds populate records, the same buttons will export the live list.")
else:
    xlsx = excel_bytes(filtered)
    pdf = pdf_bytes(filtered)
    e1,e2 = st.columns(2)
    with e1:
        st.download_button("⬇️ Export Lead List to Excel", data=xlsx, file_name=f"nyl_leads_{datetime.now().strftime('%Y%m%d')}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)
    with e2:
        st.download_button("⬇️ Export Lead List to PDF", data=pdf, file_name=f"nyl_leads_{datetime.now().strftime('%Y%m%d')}.pdf", mime="application/pdf", use_container_width=True)

st.divider()
st.subheader("Export Rules")
st.write("Exports contain the currently filtered list. Use the left-column filters to create a business-only, professional-only, COI, hot-lead, warm-lead, industry, or territory-specific export before downloading.")
st.caption("For future Salesforce integration, the master list will retain public-source provenance and deduplication keys so records can be cross-referenced without replacing the NYL system of record.")
