from __future__ import annotations

import streamlit as st

GOLD = "#D7A449"
GOLD_SOFT = "#F0C36A"
INK = "#090C11"
PANEL = "#11161D"
PANEL_2 = "#151B23"
BORDER = "#27303B"
TEXT = "#F4F7FB"
MUTED = "#98A2B3"
GREEN = "#40C463"
BLUE = "#4DA3FF"

BRAND_CSS = f"""
<style>
:root {{
    --brand-gold: {GOLD};
    --brand-gold-soft: {GOLD_SOFT};
    --brand-ink: {INK};
    --brand-panel: {PANEL};
    --brand-panel-2: {PANEL_2};
    --brand-border: {BORDER};
    --brand-text: {TEXT};
    --brand-muted: {MUTED};
}}

html, body, [data-testid="stAppViewContainer"] {{
    background:
        radial-gradient(circle at 85% 0%, rgba(215,164,73,.08), transparent 28%),
        linear-gradient(180deg, #080b10 0%, #0b1016 100%);
    color: var(--brand-text);
}}

[data-testid="stHeader"] {{ background: rgba(8,11,16,.88); border-bottom: 1px solid rgba(255,255,255,.04); }}
[data-testid="stToolbar"] {{ right: 1rem; }}

[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #070A0F 0%, #0B0F14 100%);
    border-right: 1px solid #242B34;
}}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{ color: #C8D0DA; }}
[data-testid="stSidebarNav"] a {{ border-radius: 9px; margin: 2px 8px; }}
[data-testid="stSidebarNav"] a:hover {{ background: rgba(215,164,73,.08); }}
[data-testid="stSidebarNav"] a[aria-current="page"] {{
    background: linear-gradient(90deg, rgba(215,164,73,.18), rgba(215,164,73,.04));
    border-left: 2px solid var(--brand-gold);
}}

.block-container {{
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}}

h1, h2, h3 {{ letter-spacing: -0.025em; color: #F8FAFC; }}
h1 {{ font-weight: 750; }}
h2, h3 {{ font-weight: 650; }}

[data-testid="stCaptionContainer"] {{ color: var(--brand-muted); }}

[data-testid="stMetric"] {{
    background: linear-gradient(180deg, #131921 0%, #0F141B 100%);
    border: 1px solid var(--brand-border);
    border-radius: 14px;
    padding: 18px 18px 14px 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,.22);
}}
[data-testid="stMetricLabel"] {{ color: #B9C2CE; }}
[data-testid="stMetricValue"] {{ color: #FFFFFF; }}
[data-testid="stMetricDelta"] svg {{ fill: {GREEN}; }}

.stTabs [data-baseweb="tab-list"] {{
    gap: 0;
    background: #0E1319;
    border: 1px solid var(--brand-border);
    border-radius: 12px;
    padding: 4px;
}}
.stTabs [data-baseweb="tab"] {{
    border-radius: 9px;
    color: #B6C0CB;
    padding: 12px 18px;
}}
.stTabs [aria-selected="true"] {{
    background: linear-gradient(180deg, rgba(215,164,73,.15), rgba(215,164,73,.06));
    color: var(--brand-gold-soft) !important;
}}
.stTabs [data-baseweb="tab-highlight"] {{ background-color: var(--brand-gold) !important; }}

[data-testid="stDataFrame"] {{
    border: 1px solid var(--brand-border);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,.16);
}}

[data-baseweb="input"], [data-baseweb="select"] > div,
[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input {{
    background: #0D1218 !important;
    border-color: #2A333E !important;
    color: #F5F7FA !important;
}}

.stButton > button, .stLinkButton > a {{
    border-radius: 9px !important;
    border: 1px solid #3A4653 !important;
    background: linear-gradient(180deg, #151B22, #0E1318) !important;
    color: #F4F7FA !important;
    font-weight: 600 !important;
    box-shadow: none !important;
}}
.stButton > button:hover, .stLinkButton > a:hover {{
    border-color: var(--brand-gold) !important;
    color: var(--brand-gold-soft) !important;
}}
.stButton > button[kind="primary"] {{
    background: linear-gradient(135deg, #F0C36A, #C88B2F) !important;
    color: #17120A !important;
    border-color: #E0AD52 !important;
}}

[data-testid="stAlert"] {{ border-radius: 12px; border: 1px solid #2B3541; }}
hr {{ border-color: #202832 !important; }}

.brand-lockup {{
    padding: 0.45rem 0.2rem 1.1rem 0.2rem;
    margin-bottom: .6rem;
    border-bottom: 1px solid #252C35;
}}
.brand-name {{
    font-family: Georgia, 'Times New Roman', serif;
    color: {GOLD_SOFT};
    font-size: 1.55rem;
    line-height: 1;
    letter-spacing: .08em;
    font-weight: 700;
}}
.brand-sub {{
    margin-top: .45rem;
    color: #B78941;
    font-size: .72rem;
    letter-spacing: .24em;
    font-weight: 700;
}}
.brand-person {{
    margin-top: 1rem;
    display: flex;
    gap: .7rem;
    align-items: center;
}}
.brand-avatar-placeholder {{
    width: 38px;
    height: 38px;
    border-radius: 50%;
    border: 1px solid #475261;
    display: flex;
    align-items: center;
    justify-content: center;
    color: {GOLD_SOFT};
    background: #111821;
    font-size: .8rem;
    font-weight: 800;
}}
.brand-person-name {{ color: #FFFFFF; font-weight: 700; font-size: .92rem; }}
.brand-person-role {{ color: #8F9AA7; font-size: .75rem; }}

.brand-hero {{
    background: linear-gradient(115deg, rgba(215,164,73,.10), rgba(18,24,32,.75) 42%, rgba(10,14,19,.92));
    border: 1px solid #29313B;
    border-radius: 16px;
    padding: 1.35rem 1.5rem;
    margin-bottom: 1.2rem;
}}
.brand-kicker {{ color: {GOLD_SOFT}; font-size: .74rem; letter-spacing: .16em; font-weight: 800; text-transform: uppercase; }}
.brand-hero-title {{ color: white; font-size: 1.55rem; font-weight: 750; margin-top: .22rem; }}
.brand-hero-copy {{ color: #A8B2BF; margin-top: .25rem; max-width: 850px; }}

.linkedin-card {{
    background: linear-gradient(180deg, #121923, #0E141B);
    border: 1px solid #293440;
    border-radius: 14px;
    padding: 1rem 1.15rem;
}}
.linkedin-badge {{ color: #6AB7FF; font-weight: 750; letter-spacing: .03em; }}
</style>
"""


def apply_brand_theme() -> None:
    st.markdown(BRAND_CSS, unsafe_allow_html=True)


def sidebar_brand() -> None:
    with st.sidebar:
        st.markdown(
            """
            <div class="brand-lockup">
              <div class="brand-name">CHRIS HAAKE</div>
              <div class="brand-sub">COMMAND CENTER</div>
              <div class="brand-person">
                <div class="brand-avatar-placeholder">CH</div>
                <div>
                  <div class="brand-person-name">Chris Haake</div>
                  <div class="brand-person-role">New York Life</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def brand_hero(title: str, copy: str, kicker: str = "Advisor Growth OS") -> None:
    st.markdown(
        f"""
        <div class="brand-hero">
          <div class="brand-kicker">{kicker}</div>
          <div class="brand-hero-title">{title}</div>
          <div class="brand-hero-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
