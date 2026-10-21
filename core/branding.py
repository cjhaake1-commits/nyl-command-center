from __future__ import annotations

import streamlit as st

GOLD = "#D7A449"
GOLD_SOFT = "#F0C36A"
INK = "#080B10"
PANEL = "#11161D"
PANEL_2 = "#151B23"
BORDER = "#27303B"
TEXT = "#F4F7FB"
MUTED = "#98A2B3"
GREEN = "#40C463"
BLUE = "#4DA3FF"
RED = "#FF6B6B"

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
    --brand-green: {GREEN};
    --brand-blue: {BLUE};
}}

html, body, [data-testid="stAppViewContainer"] {{
    background:
        radial-gradient(circle at 87% -8%, rgba(215,164,73,.11), transparent 28%),
        radial-gradient(circle at 12% 100%, rgba(77,163,255,.035), transparent 25%),
        linear-gradient(180deg, #070A0F 0%, #0B1016 100%);
    color: var(--brand-text);
}}

* {{ scrollbar-color: #39414C #0B0F14; }}
::selection {{ background: rgba(215,164,73,.28); color: #fff; }}

[data-testid="stHeader"] {{
    background: rgba(7,10,15,.84);
    border-bottom: 1px solid rgba(255,255,255,.04);
    backdrop-filter: blur(14px);
}}
[data-testid="stToolbar"] {{ right: 1rem; }}

/* Sidebar / product identity */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #06090D 0%, #090D12 100%);
    border-right: 1px solid #222A33;
    box-shadow: 12px 0 32px rgba(0,0,0,.12);
}}
[data-testid="stSidebarContent"] {{ padding-top: .45rem; }}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{ color: #C8D0DA; }}
[data-testid="stSidebar"] hr {{ border-color: #222A33 !important; }}

[data-testid="stSidebarNav"] {{ padding-top: .15rem; }}
[data-testid="stSidebarNav"] span {{ font-weight: 520; }}
[data-testid="stSidebarNav"] a {{
    border-radius: 9px;
    margin: 2px 8px;
    min-height: 2.55rem;
    transition: all .16s ease;
}}
[data-testid="stSidebarNav"] a:hover {{
    background: rgba(215,164,73,.075);
    transform: translateX(1px);
}}
[data-testid="stSidebarNav"] a[aria-current="page"] {{
    background: linear-gradient(90deg, rgba(215,164,73,.18), rgba(215,164,73,.035));
    border-left: 2px solid var(--brand-gold);
    box-shadow: inset 0 0 0 1px rgba(215,164,73,.06);
}}
[data-testid="stSidebarNav"] a[aria-current="page"] span {{ color: var(--brand-gold-soft) !important; }}

/* Global content rhythm */
.block-container {{
    max-width: 1540px;
    padding-top: 1.75rem;
    padding-bottom: 4rem;
    padding-left: clamp(1rem, 2.2vw, 2.25rem);
    padding-right: clamp(1rem, 2.2vw, 2.25rem);
}}

h1, h2, h3, h4 {{
    letter-spacing: -0.025em;
    color: #F8FAFC;
}}
h1 {{
    font-weight: 760;
    font-size: clamp(1.85rem, 3vw, 2.65rem);
    line-height: 1.08;
    margin-bottom: .35rem !important;
}}
h2 {{ font-weight: 690; margin-top: 1.2rem !important; }}
h3 {{ font-weight: 650; }}
h4 {{ font-weight: 625; }}
p, li {{ color: #C7CFD9; }}
strong {{ color: #F7F9FC; }}
a {{ color: var(--brand-gold-soft); }}
[data-testid="stCaptionContainer"] {{ color: var(--brand-muted); }}

/* Metrics / KPI cards */
[data-testid="stMetric"] {{
    background: linear-gradient(180deg, rgba(20,27,35,.98) 0%, rgba(14,19,26,.98) 100%);
    border: 1px solid var(--brand-border);
    border-radius: 14px;
    padding: 18px 18px 14px 18px;
    box-shadow: 0 14px 32px rgba(0,0,0,.20);
    min-height: 114px;
}}
[data-testid="stMetric"]:hover {{ border-color: #374250; }}
[data-testid="stMetricLabel"] {{ color: #B9C2CE; font-weight: 560; }}
[data-testid="stMetricValue"] {{ color: #FFFFFF; font-weight: 720; letter-spacing: -.02em; }}
[data-testid="stMetricDelta"] {{ font-weight: 600; }}
[data-testid="stMetricDelta"] svg {{ fill: {GREEN}; }}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 0;
    background: #0E1319;
    border: 1px solid var(--brand-border);
    border-radius: 12px;
    padding: 4px;
    box-shadow: 0 8px 24px rgba(0,0,0,.12);
}}
.stTabs [data-baseweb="tab"] {{
    border-radius: 9px;
    color: #B6C0CB;
    padding: 12px 18px;
    font-weight: 600;
}}
.stTabs [data-baseweb="tab"]:hover {{ color: #F0D49B; }}
.stTabs [aria-selected="true"] {{
    background: linear-gradient(180deg, rgba(215,164,73,.15), rgba(215,164,73,.055));
    color: var(--brand-gold-soft) !important;
}}
.stTabs [data-baseweb="tab-highlight"] {{ background-color: var(--brand-gold) !important; }}

/* Tables / dataframes */
[data-testid="stDataFrame"] {{
    border: 1px solid var(--brand-border);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 12px 32px rgba(0,0,0,.17);
    background: #0D1218;
}}
[data-testid="stDataFrame"] iframe {{ border-radius: 12px; }}

/* Forms and controls */
[data-testid="stForm"] {{
    background: linear-gradient(180deg, rgba(17,22,29,.90), rgba(12,17,23,.88));
    border: 1px solid var(--brand-border);
    border-radius: 14px;
    padding: 1.1rem 1.2rem 1.25rem 1.2rem;
}}
[data-baseweb="input"],
[data-baseweb="textarea"],
[data-baseweb="select"] > div,
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stDateInput"] input {{
    background: #0D1218 !important;
    border-color: #2A333E !important;
    color: #F5F7FA !important;
    border-radius: 9px !important;
}}
[data-baseweb="textarea"] textarea,
[data-testid="stTextArea"] textarea {{
    background: #0D1218 !important;
    color: #F5F7FA !important;
    border: 1px solid #2A333E !important;
    border-radius: 9px !important;
    caret-color: var(--brand-gold-soft);
}}
[data-baseweb="textarea"] textarea::placeholder,
[data-testid="stTextArea"] textarea::placeholder {{ color: #8792A0 !important; opacity: 1; }}
[data-baseweb="input"] input,
[data-baseweb="select"] input,
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stDateInput"] input {{
    background: #0D1218 !important;
    color: #F5F7FA !important;
    caret-color: var(--brand-gold-soft);
}}
[data-baseweb="select"] > div:hover,
[data-baseweb="input"]:hover,
[data-baseweb="textarea"]:hover {{ border-color: #46515E !important; }}
label, [data-testid="stWidgetLabel"] {{ color: #C7D0DB !important; font-weight: 560 !important; }}

/* Buttons */
.stButton > button, .stLinkButton > a, [data-testid="stDownloadButton"] > button {{
    border-radius: 9px !important;
    border: 1px solid #3A4653 !important;
    background: linear-gradient(180deg, #151B22, #0E1318) !important;
    color: #F4F7FA !important;
    font-weight: 620 !important;
    min-height: 2.55rem;
    box-shadow: none !important;
    transition: all .15s ease !important;
}}
.stButton > button:hover, .stLinkButton > a:hover, [data-testid="stDownloadButton"] > button:hover {{
    border-color: var(--brand-gold) !important;
    color: var(--brand-gold-soft) !important;
    transform: translateY(-1px);
}}
.stButton > button[kind="primary"],
[data-testid="stBaseButton-primary"],
[data-testid="stFormSubmitButton"] button,
button[kind="primary"] {{
    background: linear-gradient(135deg, #F0C36A 0%, #D7A449 58%, #BE8128 100%) !important;
    background-color: #D7A449 !important;
    color: #17120A !important;
    border: 1px solid #E0AD52 !important;
    font-weight: 730 !important;
}}
.stButton > button[kind="primary"]:hover,
[data-testid="stBaseButton-primary"]:hover,
[data-testid="stFormSubmitButton"] button:hover,
button[kind="primary"]:hover {{
    background: linear-gradient(135deg, #F7D58E 0%, #E1B45F 58%, #CF9439 100%) !important;
    border-color: #F0C36A !important;
    color: #17120A !important;
}}
.stButton > button:focus-visible,
.stLinkButton > a:focus-visible,
[data-testid="stDownloadButton"] > button:focus-visible,
[data-testid="stFormSubmitButton"] button:focus-visible {{
    outline: 2px solid var(--brand-gold-soft) !important;
    outline-offset: 2px !important;
}});


/* Alerts */
[data-testid="stAlert"] {{
    border-radius: 12px;
    border: 1px solid #2B3541;
    background: rgba(18,24,32,.88);
}}
[data-testid="stAlert"] p {{ color: #D3DAE3; }}

/* Expanders */
[data-testid="stExpander"] {{
    background: linear-gradient(180deg, #11171E, #0D1218);
    border: 1px solid var(--brand-border) !important;
    border-radius: 12px !important;
    overflow: hidden;
}}
[data-testid="stExpander"] summary:hover {{ color: var(--brand-gold-soft); }}

/* Progress / sliders / toggles */
[data-testid="stProgress"] > div > div > div {{ background: linear-gradient(90deg, #C88B2F, #F0C36A) !important; }}
[data-baseweb="slider"] [role="slider"] {{ background-color: var(--brand-gold-soft) !important; border-color: var(--brand-gold-soft) !important; }}
[data-baseweb="slider"] > div > div {{ background-color: rgba(215,164,73,.35); }}

/* Code / JSON / status blocks */
[data-testid="stCodeBlock"] {{
    border: 1px solid var(--brand-border);
    border-radius: 12px;
    overflow: hidden;
}}
[data-testid="stJson"] {{
    background: #0D1218;
    border: 1px solid var(--brand-border);
    border-radius: 12px;
    padding: .5rem;
}}

/* Dividers and misc */
hr {{ border-color: #202832 !important; opacity: 1 !important; }}
[data-testid="stVerticalBlockBorderWrapper"] {{ border-color: var(--brand-border) !important; border-radius: 12px; }}

/* Brand lockup */
.brand-lockup {{
    padding: 0.55rem 0.3rem 1.05rem 0.3rem;
    margin-bottom: .4rem;
    border-bottom: 1px solid #252C35;
}}
.brand-crown {{
    color: {GOLD_SOFT};
    font-size: .78rem;
    letter-spacing: .2em;
    margin-bottom: .3rem;
}}
.brand-name {{
    font-family: Georgia, 'Times New Roman', serif;
    color: {GOLD_SOFT};
    font-size: 1.38rem;
    line-height: 1;
    letter-spacing: .075em;
    font-weight: 700;
}}
.brand-sub {{
    margin-top: .45rem;
    color: #B78941;
    font-size: .68rem;
    letter-spacing: .23em;
    font-weight: 760;
}}
.brand-person {{
    margin-top: 1rem;
    display: flex;
    gap: .72rem;
    align-items: center;
    padding: .65rem;
    border: 1px solid #222B35;
    border-radius: 10px;
    background: rgba(255,255,255,.014);
}}
.brand-avatar-placeholder {{
    width: 39px;
    height: 39px;
    min-width: 39px;
    border-radius: 50%;
    border: 1px solid #465362;
    display: flex;
    align-items: center;
    justify-content: center;
    color: {GOLD_SOFT};
    background: radial-gradient(circle at 35% 30%, #1A2430, #0E141B);
    font-size: .79rem;
    font-weight: 820;
}}
.brand-person-name {{ color: #FFFFFF; font-weight: 720; font-size: .91rem; }}
.brand-person-role {{ color: #8F9AA7; font-size: .73rem; margin-top: .08rem; }}
.brand-profile-status {{
    color: #7F8A96;
    font-size: .66rem;
    margin-top: .18rem;
}}
.brand-sidebar-note {{
    margin-top: .9rem;
    padding: .8rem .75rem;
    border: 1px solid #222B35;
    border-radius: 10px;
    background: linear-gradient(180deg, rgba(215,164,73,.045), rgba(255,255,255,.008));
}}
.brand-sidebar-note-label {{ color: {GOLD_SOFT}; font-size: .64rem; letter-spacing: .13em; font-weight: 780; }}
.brand-sidebar-note-copy {{ color: #A8B1BD; font-size: .72rem; line-height: 1.45; margin-top: .3rem; }}

.brand-hero {{
    background: linear-gradient(115deg, rgba(215,164,73,.11), rgba(18,24,32,.80) 42%, rgba(10,14,19,.94));
    border: 1px solid #29313B;
    border-radius: 16px;
    padding: 1.35rem 1.5rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 14px 36px rgba(0,0,0,.16);
}}
.brand-kicker {{ color: {GOLD_SOFT}; font-size: .72rem; letter-spacing: .16em; font-weight: 820; text-transform: uppercase; }}
.brand-hero-title {{ color: white; font-size: 1.55rem; font-weight: 760; margin-top: .22rem; }}
.brand-hero-copy {{ color: #A8B2BF; margin-top: .25rem; max-width: 850px; line-height: 1.55; }}

.linkedin-card {{
    background: linear-gradient(180deg, #121923, #0E141B);
    border: 1px solid #293440;
    border-radius: 14px;
    padding: 1rem 1.15rem;
}}
.linkedin-badge {{ color: #6AB7FF; font-weight: 750; letter-spacing: .03em; }}

/* Mobile */
@media (max-width: 760px) {{
    .block-container {{ padding-top: 1.15rem; padding-left: .8rem; padding-right: .8rem; }}
    [data-testid="stMetric"] {{ min-height: 98px; padding: 14px; }}
    .brand-name {{ font-size: 1.2rem; }}
    .stTabs [data-baseweb="tab"] {{ padding: 10px 11px; font-size: .82rem; }}
    [data-testid="stForm"] {{ padding: .85rem; }}
    [data-testid="stFormSubmitButton"] button,
    [data-testid="stBaseButton-primary"] {{ width: 100%; }}
}}
@media (prefers-reduced-motion: reduce) {{
    *, *::before, *::after {{ scroll-behavior: auto !important; transition-duration: .01ms !important; animation-duration: .01ms !important; }}
}}
</style>
"""


def apply_brand_theme() -> None:
    st.markdown(BRAND_CSS, unsafe_allow_html=True)


def sidebar_brand() -> None:
    with st.sidebar:
        st.markdown(
            """
            <div class="brand-lockup">
              <div class="brand-crown">◆  ◆  ◆</div>
              <div class="brand-name">CHRIS HAAKE</div>
              <div class="brand-sub">COMMAND CENTER</div>
              <div class="brand-person">
                <div class="brand-avatar-placeholder">CH</div>
                <div>
                  <div class="brand-person-name">Chris Haake</div>
                  <div class="brand-person-role">New York Life</div>
                  <div class="brand-profile-status">Registered Representative</div>
                </div>
              </div>
              <div class="brand-sidebar-note">
                <div class="brand-sidebar-note-label">CENTRAL FLORIDA GROWTH OS</div>
                <div class="brand-sidebar-note-copy">Find. Qualify. Connect. Build generational relationships.</div>
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
