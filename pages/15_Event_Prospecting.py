from __future__ import annotations

from datetime import date, timedelta
import pandas as pd
import streamlit as st
from sqlalchemy import text
from data.db import engine, storage_backend
from core.branding import apply_brand_theme

apply_brand_theme()

from pages_event_catalog import VERIFIED_NETWORKING_EVENTS, RESEARCH_UPDATED as NETWORKING_RESEARCH_UPDATED
from booth_opportunities import BOOTH_OPPORTUNITIES, BOOTH_RESEARCH_UPDATED

def upcoming_networking():
    today = date.today()
    end = today + timedelta(days=60)
    unique = {}
    for item in VERIFIED_NETWORKING_EVENTS:
        d = date.fromisoformat(item["date"])
        if today <= d <= end:
            key = (item["date"], item["event"].strip().casefold())
            if key not in unique or item.get("importance", 0) > unique[key].get("importance", 0):
                unique[key] = item
    return sorted(unique.values(), key=lambda e: (e["date"], -e.get("importance", 0)))

EVENTS = upcoming_networking()
# These are research targets, NOT invented dated events. Dates and registration must be confirmed.
TARGETS = [
    ("Greater Orlando business chamber networking","Introductions","High"),
    ("Winter Park Chamber networking calendar","Introductions","High"),
    ("Central Florida Estate Planning Council events","Introductions","High"),
    ("Florida Institute of CPAs local CPE and networking","Introductions","High"),
    ("Orlando commercial real estate networking","Introductions","Medium"),
    ("SHRM Greater Orlando HR leadership events","Business-owner benefits","High"),
    ("Orlando SCORE small-business workshops","Business-owner benefits","Medium"),
    ("National Association of Insurance and Financial Advisors Florida events","Introductions","Medium"),
    ("Orlando entrepreneur and business-owner meetups","Business-owner benefits","Medium"),
    ("Central Florida retirement-plan advisor and benefits events","401(k) rollovers","High"),
    ("Orlando 401(k)/403(b) financial education and HR events","401(k) rollovers","High"),
]

def init_events():
    with engine().begin() as conn:
        conn.execute(text("""CREATE TABLE IF NOT EXISTS event_actions (
            event_key VARCHAR(256) PRIMARY KEY,
            status VARCHAR(40) NOT NULL DEFAULT 'Research',
            conversations INTEGER NOT NULL DEFAULT 0,
            introductions INTEGER NOT NULL DEFAULT 0,
            followups INTEGER NOT NULL DEFAULT 0,
            appointments INTEGER NOT NULL DEFAULT 0,
            notes TEXT NOT NULL DEFAULT ''
        )"""))

def get_actions():
    with engine().connect() as conn:
        return {r["event_key"]: dict(r) for r in conn.execute(text("SELECT * FROM event_actions")).mappings()}

def save_action(key,status,conversations,introductions,followups,appointments,notes):
    with engine().begin() as conn:
        conn.execute(text("""INSERT INTO event_actions (event_key,status,conversations,introductions,followups,appointments,notes)
            VALUES (:key,:status,:conversations,:introductions,:followups,:appointments,:notes)
            ON CONFLICT (event_key) DO UPDATE SET status=EXCLUDED.status, conversations=EXCLUDED.conversations,
            introductions=EXCLUDED.introductions, followups=EXCLUDED.followups,
            appointments=EXCLUDED.appointments, notes=EXCLUDED.notes"""), dict(key=key,status=status,conversations=conversations,introductions=introductions,followups=followups,appointments=appointments,notes=notes))

st.title("🤝 Event Prospecting & Introductions")
st.caption(f"{date.today():%B %d, %Y} through {(date.today() + timedelta(days=60)):%B %d, %Y} · rolling 60-day window · Central Florida")
st.info(f"{len(EVENTS)} organizer-sourced, dated networking opportunities; {len(TARGETS)} undated research targets. Organizer listing is not an RSVP or guarantee of eligibility.")
st.caption(f"Networking and Marketing use the same shared source file (catalog maintained {NETWORKING_RESEARCH_UPDATED}). Confirm RSVP and NYL requirements before attending.")

init_events()
actions=get_actions()
a,b,c,d=st.columns(4)
a.metric("Upcoming organizer-listed events",len(EVENTS))
b.metric("To verify",len(TARGETS))
c.metric("Recorded introductions",sum(int(v["introductions"]) for v in actions.values()))
d.metric("Appointments booked",sum(int(v["appointments"]) for v in actions.values()))
goal=st.multiselect("Prospecting objectives",["Introductions","401(k) rollovers","Business-owner benefits"],default=["Introductions","401(k) rollovers","Business-owner benefits"])
show_targets=st.toggle("Show unverified research targets",value=True)

rows=[]
for item in EVENTS:
    if item["objective"] in goal:
        priority = "High" if item["importance"] >= 90 else ("Medium" if item["importance"] >= 80 else "Low")
        rows.append(dict(Event=item["event"],Date=item["date"],Time=item["time"],Area=item["location"],Objective=item["objective"],Priority=priority,Verification=item.get("verification","Organizer-listed; verify RSVP"),Source=item["url"],Target_audience=item["fit"],Access=item.get("access","Confirm with organizer")))
for name,category,priority in TARGETS:
    if show_targets and category in goal:
        rows.append(dict(Event=name,Date=None,Time=None,Area="Central Florida",Objective=category,Priority=priority,Verification="Research target — no date confirmed",Source="",Target_audience="Find a future scheduled event and verify details",Access="Not a scheduled event"))
df=pd.DataFrame(rows)
st.dataframe(df,hide_index=True,use_container_width=True,column_config={"Source":st.column_config.LinkColumn("Source / RSVP")})
st.download_button("Download prospecting research CSV",df.to_csv(index=False).encode(),file_name=f"nyl_event_prospecting_{date.today():%Y%m%d}.csv",mime="text/csv")

st.subheader("Booth and Exhibitor Research - shared calendar")
st.caption(f"Potential applications and sponsor inquiries, not reservations. Booth sources reviewed {BOOTH_RESEARCH_UPDATED}; verify each deadline, category rules and NYL compliance approval.")
date_from, date_to = date.today(), date.today() + timedelta(days=60)
booth_rows = [b for b in BOOTH_OPPORTUNITIES if date_from <= date.fromisoformat(b["date"]) <= date_to]
booth_rows = sorted({(b["date"], b["event"].casefold()): b for b in booth_rows}.values(), key=lambda b: b["date"])
if booth_rows:
    st.dataframe(pd.DataFrame(booth_rows)[["date","event","location","participation_type","application_deadline","application_status","fit","url"]],hide_index=True,use_container_width=True,column_config={"url": st.column_config.LinkColumn("Official application / inquiry")})
st.caption(f"{len(booth_rows)} dated booth/sponsorship leads. Some organizers allow financial planning or commercial services in principle; no NYL-specific booth acceptance or compliance approval is confirmed.")

st.subheader("Event action plan")
st.markdown("""**Before:** Verify organizer details and NYL requirements; RSVP; identify 3–5 relevant professional or business-owner roles; prepare two non-product opening questions.
**At event:** Focus on personal introductions, listen for planning triggers, request permission to reconnect; avoid collecting sensitive client data.
**Within 24–48 hours:** Send individually reviewed follow-up through approved channels; offer a discovery meeting; request a warm introduction only with permission.
**Track:** Conversations → permission-based introductions → follow-ups → appointments. These are activity measurements, not promised sales.
**Compliance:** No investment recommendations, client financial details, automatic outreach, or Salesforce exports from this module. Confirm NYL rules on events, advertising, gifts and recordkeeping.""")
st.caption("Suggested per-event target: 5 substantive conversations, 2 permission-based introductions, 3 follow-ups, 1 meeting. Adjustable goals, not performance claims.")

st.subheader("Record an event outcome")
names=[x["Event"] for x in rows]
if names:
    chosen=st.selectbox("Event / research target",names)
    current=actions.get(chosen,{})
    with st.form("event_action"):
        status_options=["Research","RSVP pending","Registered","Attended","Follow-up","Completed","Declined"]
        status=st.selectbox("Status",status_options,index=status_options.index(current.get("status","Research")) if current.get("status","Research") in status_options else 0)
        p,q,r,s=st.columns(4)
        conversations=p.number_input("Conversations",min_value=0,value=int(current.get("conversations",0)))
        introductions=q.number_input("Introductions",min_value=0,value=int(current.get("introductions",0)))
        followups=r.number_input("Follow-ups",min_value=0,value=int(current.get("followups",0)))
        appointments=s.number_input("Appointments",min_value=0,value=int(current.get("appointments",0)))
        notes=st.text_area("Non-sensitive notes only",value=current.get("notes",""))
        if st.form_submit_button("Save activity"):
            save_action(chosen,status,int(conversations),int(introductions),int(followups),int(appointments),notes)
            st.success("Event activity saved.")
            st.rerun()
st.caption(f"Storage: {storage_backend()}. SQLite fallback on Streamlit Cloud may be temporary; use configured PostgreSQL for persistent outcomes.")
