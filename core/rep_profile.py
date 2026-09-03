from __future__ import annotations

REP_NAME = "David Beck"
REP_INITIALS = "DB"
COMPANY_NAME = "New York Life"
APP_TITLE = "David Beck Command Center"
STREAMLIT_APP_NAME = "david-beck-command-center"

TERRITORY_ZIP = "93065"
TERRITORY_CITY = "Simi Valley"
TERRITORY_STATE = "CA"
TERRITORY_RADIUS_MILES = 20
TERRITORY_LABEL = "Simi Valley + 20-mile radius"
TERRITORY_GROWTH_LABEL = "SIMI VALLEY GROWTH OS"

USER_EMAIL = "pdavidbeck@gmail.com"

# Keep the same operating model as the original NYL Command Center while
# making geography and identity tenant-specific.
PROFILE = {
    "rep_name": REP_NAME,
    "rep_initials": REP_INITIALS,
    "company": COMPANY_NAME,
    "app_title": APP_TITLE,
    "streamlit_app_name": STREAMLIT_APP_NAME,
    "email": USER_EMAIL,
    "territory": {
        "zip": TERRITORY_ZIP,
        "city": TERRITORY_CITY,
        "state": TERRITORY_STATE,
        "radius_miles": TERRITORY_RADIUS_MILES,
        "label": TERRITORY_LABEL,
    },
}
