from __future__ import annotations

import streamlit as st

from core.branding import brand_hero
from core.business_networking_desk import render_business_networking_desk

st.set_page_config(page_title="Business & Networking Desk | Chris Haake", page_icon="🏢", layout="wide")
brand_hero(
    "Business & Networking Desk",
    "Official Florida business lookup, regional research links, and practical conversation prep for calls and events.",
    "Chris Haake • New York Life",
)
render_business_networking_desk()
