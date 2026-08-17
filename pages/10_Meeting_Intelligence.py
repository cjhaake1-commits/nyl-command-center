from __future__ import annotations

from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Meeting Intelligence", page_icon="🎙️", layout="wide")
st.title("Meeting Intelligence")
st.caption("Upload a recording from your phone, preserve the meeting context, and turn approved recordings into structured follow-up intelligence.")

st.warning("Before recording or uploading any meeting, confirm applicable consent requirements and NYL privacy/compliance rules. Do not upload nonpublic client information to an external AI workflow unless NYL authorizes it.")

meeting_type = st.selectbox("Meeting type", ["Prospect / client", "NYL internal / training", "COI / networking", "Recruiting / interview", "Other"])
meeting_name = st.text_input("Meeting / account name")
meeting_date = st.date_input("Meeting date")
consent = st.checkbox("I have confirmed that recording and AI processing are permitted for this meeting.")

st.markdown("### 🎙️ Upload meeting recording")
audio = st.file_uploader("Choose the recording from your phone", type=["m4a", "mp3", "wav", "mp4", "aac", "ogg"])
if audio:
    st.audio(audio)
    st.success(f"Recording selected: {audio.name}")

st.markdown("### Analysis Pack")
items = [
    "Executive summary and meeting outcome",
    "Facts, goals and priorities explicitly stated",
    "Questions asked and questions left unanswered",
    "Potential planning topics for human review",
    "Objections, hesitation and decision criteria",
    "People, companies and possible introduction paths mentioned",
    "Commitments made by each party",
    "Documents / information requested",
    "Recommended next questions",
    "Dated next actions",
    "CRM-ready meeting note",
    "What did I miss? — missed follow-up questions, unresolved issues and weak transitions",
]
for item in items:
    st.write(f"• {item}")

st.markdown("### Meeting Coach")
st.caption("Once transcription/analysis is connected, this section will learn from meetings over time rather than scoring from assumptions alone.")
c1,c2,c3,c4 = st.columns(4)
c1.metric("Discovery depth", "—")
c2.metric("Next-step clarity", "—")
c3.metric("Objections resolved", "—")
c4.metric("Introduction opportunity", "—")

if st.button("Analyze Recording", type="primary", disabled=not (audio and consent)):
    st.info("Upload intake is ready. The transcription/AI processing connector must be configured before audio can be analyzed automatically inside the app. Until NYL policy is known, recordings are not automatically sent to an external AI service.")

st.divider()
st.subheader("Structured Debrief Workspace")
st.text_area("Transcript / notes", height=180, placeholder="Paste a transcript or notes here when available.")
st.text_area("Key facts and goals", height=100)
st.text_area("Potential opportunities / topics to investigate", height=100)
st.text_area("Objections / concerns", height=100)
st.text_area("Commitments and next actions", height=100)
st.text_area("What did I miss?", height=120)
st.caption(f"Meeting Intelligence workspace • {datetime.now().strftime('%Y-%m-%d')}")
