from __future__ import annotations
import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from core.branding import apply_brand_theme
from rollover_playbook_content import GUIDE

apply_brand_theme()
st.title("401(k) Rollover Execution Playbook")
st.caption("Internal advisor SOP and checklists | NYL / NYLIFE Securities | Review against current firm procedures")
st.warning("Internal training aid only. Product recommendations, securities activities, disclosures and compensation require current firm approval and applicable registration.")
st.download_button("Download complete rollover playbook (Markdown)", GUIDE.encode("utf-8"), "NYL_Rollover_Execution_Playbook.md", "text/markdown")

def make_pdf():
    buf=BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=letter,rightMargin=49,leftMargin=49,topMargin=50,bottomMargin=49)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name="PlayTitle",parent=styles["Title"],fontSize=19,leading=24,textColor=HexColor("#12344A"),spaceAfter=14))
    styles.add(ParagraphStyle(name="PlayH",parent=styles["Heading2"],fontSize=12,leading=16,textColor=HexColor("#175A73"),spaceBefore=14,spaceAfter=6))
    styles.add(ParagraphStyle(name="PlayBody",parent=styles["BodyText"],fontSize=9.5,leading=14,spaceAfter=6))
    story=[]
    import html
    for raw in GUIDE.splitlines():
        line=raw.strip()
        if not line: story.append(Spacer(1,5));continue
        if line.startswith("# "): style=styles["PlayTitle"];line=line[2:]
        elif line.startswith("## "): style=styles["PlayH"];line=line[3:]
        else: style=styles["PlayBody"]
        line=html.escape(line).replace("**","")
        if line.startswith("- [ ] "): line="&#9633; "+line[6:]
        story.append(Paragraph(line,style))
    doc.build(story)
    return buf.getvalue()

st.download_button("Download printable PDF",make_pdf(),file_name="NYL_Rollover_Execution_Playbook.pdf",mime="application/pdf")
for section in GUIDE.split("\n## "):
    if section.startswith("# "):
        st.markdown(section)
    else:
        heading,_,body=section.partition("\n")
        with st.expander(heading,expanded=heading.startswith("1.")):
            st.markdown(body)
