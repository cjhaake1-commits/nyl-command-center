from __future__ import annotations

import streamlit as st

from core.branding import brand_hero
from core.subject_briefing import render_subject_briefing

st.set_page_config(page_title="Quick Subject Briefing | Chris Haake", page_icon="🔍", layout="wide")
brand_hero(
    "Quick Subject Briefing",
    "Prepare for conversations with concise, source-linked public information on a person, business, organization, or topic.",
    "Chris Haake • New York Life",
)
render_subject_briefing()
