from __future__ import annotations

from datetime import date, datetime
from zoneinfo import ZoneInfo
import importlib

import pandas as pd
import streamlit as st

from core.branding import apply_brand_theme

apply_brand_theme()
import pages_event_catalog
pages_event_catalog = importlib.reload(pages_event_catalog)

TZ = ZoneInfo("America/New_York")
today = datetime.now(TZ).date()
events = pages_event_catalog.VERIFIED_NETWORKING_EVENTS

st.title("🗓️ Event Schedule")
st.caption("Verified organizer-listed networking events from the shared event catalog. Orange County is prioritized as your home market.")
st.caption(f"Catalog checked {pages_event_catalog.RESEARCH_UPDATED}. Confirm registration, access, and NYL requirements with the organizer.")

horizon = st.selectbox("Show events", ["Next 30 days", "Next 60 days", "All upcoming"], index=1)
days = {"Next 30 days": 30, "Next 60 days": 60}.get(horizon)
end_date = today + pd.Timedelta(days=days) if days else None

def market_for(item):
    text = f"{item.get('organization', '')} {item.get('location', '')}".casefold()
    if any(term in text for term in ("orlando", "winter park", "dr. phillips", "dr phillips", "west orange", "winter garden", "windermere", "horizon west", "ocoee", "apopka", "maitland")):
        return "Orange County"
    if "seminole" in text or any(term in text for term in ("lake mary", "sanford", "oviedo", "altamonte", "casselberry", "heathrow")):
        return "Seminole County"
    if "osceola" in text or any(term in text for term in ("kissimmee", "celebration")):
        return "Osceola County"
    if any(term in text for term in ("clermont", "leesburg", "lake county")):
        return "Lake County"
    return "Central Florida"

rows = []
for item in events:
    event_date = date.fromisoformat(item["date"])
    if event_date < today or (end_date and event_date > end_date):
        continue
    rows.append({
        "Date": event_date.isoformat(),
        "Time": item.get("time", "See organizer"),
        "Market": market_for(item),
        "Event": item["event"],
        "Organizer": item.get("organization", ""),
        "Location": item.get("location", ""),
        "Fit": item.get("fit", ""),
        "Access / cost": item.get("access", "Confirm with organizer"),
        "Verification": item.get("verification", "Organizer-listed; verify current details"),
        "Source / RSVP": item.get("url", ""),
        "_importance": item.get("importance", 0),
    })

market_order = {"Orange County": 0, "Seminole County": 1, "Osceola County": 2, "Lake County": 3, "Central Florida": 4}
df = pd.DataFrame(rows)
if not df.empty:
    df["_market_order"] = df["Market"].map(market_order).fillna(4)
    df = df.sort_values(["_market_order", "Date", "_importance"], ascending=[True, True, False])
    df = df.drop(columns=["_market_order", "_importance"])

st.metric("Scheduled opportunities", len(df))
if df.empty:
    st.info("No catalogued events fall within this date range. Check the live search links on Event Prospecting for current listings.")
else:
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,
        column_config={"Source / RSVP": st.column_config.LinkColumn("Source / RSVP")},
    )
    st.download_button(
        "Download schedule CSV",
        df.to_csv(index=False).encode("utf-8"),
        file_name=f"nyl_event_schedule_{today:%Y%m%d}.csv",
        mime="text/csv",
    )

st.markdown("**Orange County calendars:** [West Orange Chamber](https://biz.wochamber.com/events/) · [Orlando Chamber](https://my.orlandochamberofcommerce.com/events) · [Winter Park Chamber](https://business.winterpark.org/events/) · [Dr. Phillips Chamber](https://drphillipschamber.org/organizer/dr-phillips-chamber-of-commerce/)")
st.warning("Listings are public organizer information, not confirmed attendance or eligibility. Verify current date, venue, registration, fees, and New York Life approval before attending or conducting business.")
