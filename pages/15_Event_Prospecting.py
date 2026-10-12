from __future__ import annotations

from datetime import date, timedelta
import pandas as pd
import streamlit as st
from sqlalchemy import text
from data.db import engine, storage_backend
from core.branding import apply_brand_theme

apply_brand_theme()

EVENTS = [
    ("2026 Leadership Forum: Shaping Central Florida's Future","2026-10-13","18:00","Orlando","Introductions","High","Confirmed","https://www.orlandochamberofcommerce.com/events.php?cal_m=10&cal_y=2026","Executives and local business leaders"),
    ("Pink Martini Party & Casino Night — American Cancer Society","2026-10-14","16:30","Orlando","Introductions","Medium","Confirmed","https://www.orlandochamberofcommerce.com/events.php?cal_m=10&cal_y=2026","Philanthropic connectors; relationship-building, not solicitation"),
    ("Coldwell Banker Realty SW Orlando Grand Opening","2026-10-15","15:00","Orlando","Introductions","High","Confirmed","https://www.orlandochamberofcommerce.com/events.php?cal_m=10&cal_y=2026","Realtors, brokers, mortgage-related referral partners"),
    ("Orlando Business Social at Bainbridge International","2026-10-15","18:00","Orlando","Introductions","High","Confirmed","https://my.orlandochamberofcommerce.com/event-6851746","Business owners, professionals and referral partners"),
    ("The Road Ahead: A Town Hall with Chris Messina","2026-10-20","15:00","Orlando","Business-owner benefits","Medium","Confirmed","https://www.orlandochamberofcommerce.com/events.php?cal_m=10&cal_y=2026&lang=en","Business policy and community leadership contacts"),
    ("Orlando Business Social at Red Bowl Asian Bistro","2026-10-22","18:00","Winter Park","Introductions","High","Confirmed","https://www.orlandochamberofcommerce.com/events.php?cal_m=10&cal_y=2026","Professional contacts and small business decision-makers"),
    ("Orlando Business Social at Dick's Last Resort","2026-10-29","18:00","Orlando","Introductions","Medium","Confirmed","https://my.orlandochamberofcommerce.com/Events","Business network and professional introductions"),
    ("Lunch and Learn: How Well Do You Know Your Bench?","2026-11-10","12:00","Orlando","Business-owner benefits","High","Confirmed","https://my.orlandochamberofcommerce.com/Events","Succession, leadership continuity and employer solutions"),
    ("7 Brew Coffee Grand Opening","2026-11-17","10:30","Orlando","Business-owner benefits","Low","Confirmed","https://www.orlandochamberofcommerce.com/events.php?cal_m=10&cal_y=2026&lang=en","Franchise owners and local business relationships"),
]
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
st.caption("October 12 – December 12, 2026 · Central Florida · NYL-aligned prospecting research")
st.info("9 source-listed events + 11 research targets. Research targets are **not confirmed events** and have no invented dates. Verify event status, details and RSVP before travel. Event times shown in local Eastern Time.")
st.caption("Source-backed events use the Orlando Chamber calendar. Some provider listings conflict on venue details; confirm with the organizer.")

init_events()
actions=get_actions()
a,b,c,d=st.columns(4)
a.metric("Confirmed event listings",len(EVENTS))
b.metric("To verify",len(TARGETS))
c.metric("Recorded introductions",sum(int(v["introductions"]) for v in actions.values()))
d.metric("Appointments booked",sum(int(v["appointments"]) for v in actions.values()))
goal=st.multiselect("Prospecting objectives",["Introductions","401(k) rollovers","Business-owner benefits"],default=["Introductions","401(k) rollovers","Business-owner benefits"])
show_targets=st.toggle("Show unverified research targets",value=True)

rows=[]
for name,day,time_,city,category,priority,verification,url,audience in EVENTS:
    if category in goal:
        rows.append(dict(Event=name,Date=day,Time=time_,Area=city,Objective=category,Priority=priority,Verification=verification,Source=url,Target_audience=audience))
for name,category,priority in TARGETS:
    if show_targets and category in goal:
        rows.append(dict(Event=name,Date=None,Time=None,Area="Central Florida",Objective=category,Priority=priority,Verification="Research target — no date confirmed",Source="",Target_audience="Find a future scheduled event and verify details"))
df=pd.DataFrame(rows)
st.dataframe(df,hide_index=True,use_container_width=True,column_config={"Source":st.column_config.LinkColumn("Source / RSVP")})
st.download_button("Download prospecting research CSV",df.to_csv(index=False).encode(),file_name="nyl_event_prospecting_oct_dec_2026.csv",mime="text/csv")

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
