from __future__ import annotations

from datetime import datetime
from io import BytesIO
import html

import pandas as pd
import streamlit as st

from core.rep_profile import REP_NAME, TERRITORY_LABEL

st.set_page_config(page_title="Lead Delivery", page_icon="📋", layout="wide")
st.title("Lead Delivery")
st.caption(f"{REP_NAME} • {TERRITORY_LABEL} • research-only until separately authorized for outreach")

SALESFORCE_COLUMNS = [
    "First Name",
    "Middle Name",
    "Last Name",
    "Source",
    "Sub-Source",
    "Target Segment",
    "Home Phone",
    "Mobile Phone",
    "Work Phone",
    "Personal Email",
    "Work Email",
    "Other Email",
    "Date Of Birth",
    "Gender",
    "Street",
    "City",
    "State",
    "Postal Code",
]

SCRIPT_COLUMNS = [
    "First Name",
    "Last Name",
    "Company",
    "Role",
    "Selection Rationale",
    "Cold Call Introduction",
    "Introduction Email Subject",
    "Introduction Email",
    "Compliance Status",
]


def blank_salesforce_df() -> pd.DataFrame:
    return pd.DataFrame(columns=SALESFORCE_COLUMNS)


def ensure_salesforce_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in SALESFORCE_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    return out[SALESFORCE_COLUMNS]


def split_name(first: str, last: str) -> str:
    return " ".join(x for x in [str(first).strip(), str(last).strip()] if x)


def make_script_record(row: pd.Series) -> dict[str, str]:
    first = str(row.get("First Name", "")).strip()
    last = str(row.get("Last Name", "")).strip()
    name = split_name(first, last) or "there"
    company = str(row.get("Company", "")).strip()
    role = str(row.get("Role", "")).strip()
    rationale = str(row.get("Sub-Source", "")).strip() or str(row.get("Selection Rationale", "")).strip()

    context_bits = []
    if company:
        context_bits.append(company)
    if role:
        context_bits.append(role)
    context = " / ".join(context_bits)

    call = (
        f"Hi {first or name}, this is {REP_NAME}. I’ll keep this brief. "
        + (f"I came across you through your work with {company}. " if company else "I came across your professional background locally. ")
        + (f"What caught my attention was {rationale.rstrip('.')} . " if rationale else "I’m making a point of getting to know more business owners and professionals in the area. ")
        + "I’m not calling to pitch you anything today. I work with New York Life and spend a lot of time getting to know local owners and professionals around long-term planning, protection, and business continuity. "
        + "I thought it would be worthwhile to introduce myself and learn a little more about what you’re working on. Would you be open to a short coffee or introductory conversation sometime in the next couple of weeks?"
    )

    subject = f"Introduction — {REP_NAME} / New York Life"
    email_body = (
        f"Hi {first or name},\n\n"
        + (f"I came across your work with {company}" + (f" as {role}" if role else "") + ". " if company else "I came across your professional background in the Simi Valley area. ")
        + (f"{rationale.rstrip('.')} stood out to me. " if rationale else "I’ve been making a point of getting to know more owners and professionals in the area. ")
        + "I’m not reaching out to turn this into an insurance presentation. I work with New York Life and focus on building relationships with business owners and professionals around long-term planning, protection, business continuity, succession, executive and employee benefits, and broader financial planning when appropriate.\n\n"
        + "I’d enjoy introducing myself and learning more about what you’re working on. If you’re open to it, perhaps we could grab coffee or have a brief introductory call sometime in the next couple of weeks.\n\n"
        + f"Best,\n{REP_NAME}\nNew York Life"
    )

    return {
        "First Name": first,
        "Last Name": last,
        "Company": company,
        "Role": role,
        "Selection Rationale": rationale,
        "Cold Call Introduction": call,
        "Introduction Email Subject": subject,
        "Introduction Email": email_body,
        "Compliance Status": "HOLD — RESEARCH ONLY / COMPLIANCE REVIEW",
    }


def xlsx_bytes(df: pd.DataFrame, sheet_name: str) -> bytes:
    out = BytesIO()
    with pd.ExcelWriter(out, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
        ws = writer.book[sheet_name]
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for cells in ws.columns:
            width = max((len(str(c.value)) if c.value is not None else 0) for c in cells)
            ws.column_dimensions[cells[0].column_letter].width = min(max(width + 2, 12), 48)
    return out.getvalue()


def scripts_pdf_bytes(df: pd.DataFrame) -> bytes:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=letter, leftMargin=42, rightMargin=42, topMargin=42, bottomMargin=42)
    styles = getSampleStyleSheet()
    body = ParagraphStyle("Body2", parent=styles["BodyText"], leading=15, spaceAfter=8, alignment=TA_LEFT)
    story = [Paragraph(f"{REP_NAME} — Personalized Prospect Scripts", styles["Title"]), Spacer(1, 10)]

    for i, row in df.iterrows():
        full_name = split_name(row.get("First Name", ""), row.get("Last Name", "")) or "Prospect"
        company = str(row.get("Company", "")).strip()
        story.append(Paragraph(html.escape(full_name + (f" — {company}" if company else "")), styles["Heading2"]))
        story.append(Paragraph("<b>Why selected</b>", styles["Heading3"]))
        story.append(Paragraph(html.escape(str(row.get("Selection Rationale", ""))), body))
        story.append(Paragraph("<b>Cold-call introduction</b>", styles["Heading3"]))
        story.append(Paragraph(html.escape(str(row.get("Cold Call Introduction", ""))), body))
        story.append(Paragraph("<b>Introduction email</b>", styles["Heading3"]))
        story.append(Paragraph(html.escape(str(row.get("Introduction Email Subject", ""))), body))
        story.append(Paragraph(html.escape(str(row.get("Introduction Email", ""))).replace("\n", "<br/>"), body))
        story.append(Paragraph("<b>Status:</b> HOLD — research only / compliance review", body))
        if i < len(df) - 1:
            story.append(PageBreak())

    doc.build(story)
    return output.getvalue()


if "paul_salesforce_ready" not in st.session_state:
    st.session_state.paul_salesforce_ready = blank_salesforce_df()

if "paul_script_context" not in st.session_state:
    st.session_state.paul_script_context = pd.DataFrame(columns=["First Name", "Last Name", "Company", "Role", "Sub-Source"])

salesforce_tab, scripts_tab = st.tabs(["Salesforce Ready Import", "Personalized Scripts"])

with salesforce_tab:
    st.subheader("Salesforce Ready Import")
    st.caption("Only net-new, verified, import-ready contacts should be placed here. The table preserves the same 18-column Salesforce import structure used in the original NYL Command Center.")
    st.info("Unknown fields stay blank. Public/professional contact routes only. Do not use home-address-derived personal outreach data. Outreach remains HOLD unless separately authorized.")

    edited = st.data_editor(
        ensure_salesforce_columns(st.session_state.paul_salesforce_ready),
        num_rows="dynamic",
        width="stretch",
        hide_index=True,
        key="paul_salesforce_editor",
    )

    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("Save Salesforce List", type="primary", use_container_width=True):
            st.session_state.paul_salesforce_ready = ensure_salesforce_columns(edited)
            st.success("Salesforce-ready list saved for this session.")
    with c2:
        st.metric("Import-ready rows", len(edited))
    with c3:
        contactable = 0
        if not edited.empty:
            contactable = int(
                edited[["Home Phone", "Mobile Phone", "Work Phone", "Personal Email", "Work Email", "Other Email"]]
                .fillna("")
                .astype(str)
                .apply(lambda r: any(v.strip() for v in r), axis=1)
                .sum()
            )
        st.metric("With contact route", contactable)

    if not edited.empty:
        st.download_button(
            "Download Salesforce Ready Import (.xlsx)",
            xlsx_bytes(ensure_salesforce_columns(edited), "Salesforce Import"),
            f"Paul_Deck_Salesforce_Ready_{datetime.now().strftime('%Y-%m-%d')}.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

with scripts_tab:
    st.subheader("Personalized Scripts")
    st.caption("One-to-one relationship-first call and email language for the exact contacts in the Salesforce-ready block.")

    source = ensure_salesforce_columns(st.session_state.paul_salesforce_ready)
    if source.empty:
        st.info("No Salesforce-ready contacts have been loaded yet. Once leads are added, this tab will create a matched script package for the same people.")
    else:
        extra = st.session_state.paul_script_context.copy()
        scripts = []
        for _, row in source.iterrows():
            first = str(row.get("First Name", "")).strip()
            last = str(row.get("Last Name", "")).strip()
            match = pd.DataFrame()
            if not extra.empty:
                match = extra[
                    extra["First Name"].astype(str).str.strip().str.casefold().eq(first.casefold())
                    & extra["Last Name"].astype(str).str.strip().str.casefold().eq(last.casefold())
                ]
            combined = row.copy()
            if not match.empty:
                m = match.iloc[0]
                combined["Company"] = m.get("Company", "")
                combined["Role"] = m.get("Role", "")
                if not str(combined.get("Sub-Source", "")).strip():
                    combined["Sub-Source"] = m.get("Sub-Source", "")
            scripts.append(make_script_record(combined))

        scripts_df = pd.DataFrame(scripts, columns=SCRIPT_COLUMNS)

        for _, row in scripts_df.iterrows():
            full_name = split_name(row["First Name"], row["Last Name"])
            with st.expander(full_name or "Prospect"):
                st.markdown(f"**Why selected:** {row['Selection Rationale'] or 'Rationale pending research enrichment.'}")
                st.markdown("**Cold-call introduction**")
                st.write(row["Cold Call Introduction"])
                st.markdown("**Introduction email**")
                st.write(row["Introduction Email Subject"])
                st.text(row["Introduction Email"])
                st.caption(row["Compliance Status"])

        st.download_button(
            "Download Personalized Scripts (.pdf)",
            scripts_pdf_bytes(scripts_df),
            f"Paul_Deck_Personalized_Scripts_{datetime.now().strftime('%Y-%m-%d')}.pdf",
            "application/pdf",
            use_container_width=True,
        )

st.divider()
st.caption("This page is a delivery surface. Prospect research, source verification, duplicate control, suitability, licensing, and NYL compliance review remain separate controls.")
