from __future__ import annotations

from datetime import date, datetime, timezone
from io import BytesIO
import json

import pandas as pd
import streamlit as st

from core.branding import apply_brand_theme
from data.community_hub import (
    add_event, import_csv_rows, init_community_tables, list_events,
    list_prospects, list_requests, save_prospect, submit_request,
)

apply_brand_theme()
REP_EMAIL = "Ashley profile pending"
REP_NAME = "Ashley"
init_community_tables()

EQUINE = [
    {"segment":"Ocala Equine","name":"Ocala CEP Equine Initiative","organization":"Ocala/Marion County economic partnership","city":"Ocala","state":"FL","contact_route":"Official Equine Initiative page","source_url":"https://ocalacep.com/programs/equine","qualification_status":"Organization / public route","permission_status":"Ask how non-member professionals may participate","notes":"Monthly partner meeting; programs open to CEP partners."},
    {"segment":"Ocala Equine","name":"Ocala Horse Alliance","organization":"Marion County horse-industry network","city":"Ocala","state":"FL","contact_route":"Official contact/membership route","source_url":"https://ocalahorsealliance.com/","qualification_status":"Organization / public route","permission_status":"Ask about membership, educational seminars and event rules","notes":"Broad industry membership spanning disciplines and related businesses."},
    {"segment":"Ocala Equine","name":"World Equestrian Center — Ocala","organization":"Equestrian venue and event organizer","city":"Ocala","state":"FL","contact_route":"Official events / partnership routes","source_url":"https://worldequestriancenter.com/ocala-fl/equestrian/shows/","qualification_status":"Event / organization route","permission_status":"Confirm public access and commercial participation rules","notes":"Shows offer public spectator access; venue access is not permission to solicit."},
    {"segment":"Ocala Equine","name":"Florida Horse Park","organization":"Equestrian and community event facility","city":"Ocala","state":"FL","contact_route":"Official calendar / contact route","source_url":"https://floridahorsepark.com/","qualification_status":"Event / organization route","permission_status":"Ask about public events and volunteer pathways","notes":"Multiple disciplines and community events."},
    {"segment":"Ocala Equine","name":"HITS Post Time Farm — Ocala","organization":"Hunter / jumper / dressage show venue","city":"Ocala","state":"FL","contact_route":"Official HITS show calendar","source_url":"https://www.hitsshows.com/ocala","qualification_status":"Event / organization route","permission_status":"Confirm current schedule and access","notes":"Use organizer-approved networking or sponsorship routes."},
    {"segment":"Ocala Equine","name":"Marion County Farm Bureau","organization":"Agriculture and farm-owner network","city":"Ocala","state":"FL","contact_route":"Official county office route","source_url":"https://marioncountyfarmbureau.com/","qualification_status":"Organization / COI route","permission_status":"Ask about public member events and guest rules","notes":"Potential agriculture ecosystem route; equestrian relevance must be established in conversation."},
    {"segment":"Ocala Equine","name":"Florida Thoroughbred Breeders’ and Owners’ Association","organization":"Thoroughbred industry organization","city":"Ocala","state":"FL","contact_route":"Official organization route","source_url":"https://ftboa.com/","qualification_status":"Organization / COI route","permission_status":"Ask about public education and industry events","notes":"Professional industry network; follow event and membership policies."},
]

STARTER_EVENTS = [
    {"title":"WEC Ocala November Series I","organizer":"World Equestrian Center — Ocala","start_date":"2026-11-04","end_date":"2026-11-08","start_time":"See official schedule","location":"1750 NW 80th Ave, Ocala, FL","event_type":"Equestrian / hunter-jumper","source_url":"https://worldequestriancenter.com/ocala-fl/equestrian/shows/november-december-show-series/","status":"Organizer-listed — confirm details","notes":"Public spectator event; business solicitation, sponsorship or exhibitor activity requires venue/firm permission."},
    {"title":"Ocala Food & Wine Festival","organizer":"World Equestrian Center — Ocala","start_date":"2026-11-06","end_date":"2026-11-08","start_time":"See official schedule","location":"World Equestrian Center, Ocala, FL","event_type":"Community / equestrian venue","source_url":"https://worldequestriancenter.com/ocala-fl/equestrian/shows/november-december-show-series/","status":"Organizer-listed — ticketed; confirm","notes":"Attend as a guest; no attendee prospecting."},
    {"title":"WEC Ocala November Series II","organizer":"World Equestrian Center — Ocala","start_date":"2026-11-11","end_date":"2026-11-15","start_time":"See official schedule","location":"1750 NW 80th Ave, Ocala, FL","event_type":"Equestrian / hunter-jumper","source_url":"https://worldequestriancenter.com/ocala-fl/equestrian/shows/november-december-show-series/","status":"Organizer-listed — confirm details","notes":"Public spectator event; use approved professional networking routes only."},
    {"title":"Ocala Polo Fall Season","organizer":"Ocala Polo Club / Florida Horse Park","start_date":"2026-11-14","end_date":"2026-11-14","start_time":"Confirm with organizer","location":"Florida Horse Park, 11008 S Hwy 475, Ocala, FL","event_type":"Equestrian / polo","source_url":"https://www.ocalamarion.com/things-to-do/equestrian/horse-shows-events/","status":"Local tourism calendar listing — verify","notes":"Date and event details should be reconfirmed before travel."},
    {"title":"HITS Post Time Dressage","organizer":"HITS Ocala","start_date":"2026-11-21","end_date":"2026-11-22","start_time":"See organizer","location":"HITS Post Time Farm, Ocala, FL","event_type":"Equestrian / dressage","source_url":"https://www.ocalamarion.com/things-to-do/equestrian/horse-shows-events/","status":"Local tourism calendar listing — verify","notes":"Confirm current schedule and spectator access."},
    {"title":"AHAF Holiday Festival Arabian & Half Arabian Horse Show","organizer":"Arabian Horse Association of Florida","start_date":"2026-11-25","end_date":"2026-11-28","start_time":"8:00 AM–4:00 PM","location":"World Equestrian Center, 1750 NW 80th Ave, Ocala, FL","event_type":"Equestrian / Arabian show","source_url":"https://www.bbs.ocalamarion.com/events/ahaf-holiday-festival-arabian-half-arabian-horse-show/","status":"Organizer / tourism listing — verify","notes":"Free family event per listing."},
    {"title":"WEC Winter Wonderland","organizer":"World Equestrian Center — Ocala","start_date":"2026-11-27","end_date":"2026-12-23","start_time":"3:00–9:00 PM on listed dates","location":"World Equestrian Center, Ocala, FL","event_type":"Community / holiday","source_url":"https://worldequestriancenter.com/ocala-fl/equestrian/shows/november-december-show-series/","status":"Organizer-listed — ticketed; confirm","notes":"Holiday public event; no attendee prospecting."},
    {"title":"WEC Ocala December Series I","organizer":"World Equestrian Center — Ocala","start_date":"2026-12-01","end_date":"2026-12-06","start_time":"See official schedule","location":"1750 NW 80th Ave, Ocala, FL","event_type":"Equestrian / FEI show jumping","source_url":"https://worldequestriancenter.com/ocala-fl/equestrian/shows/november-december-show-series/","status":"Organizer-listed — confirm details","notes":"Public spectator event; confirm current access."},
    {"title":"WEC Ocala December Series II","organizer":"World Equestrian Center — Ocala","start_date":"2026-12-08","end_date":"2026-12-13","start_time":"See official schedule","location":"1750 NW 80th Ave, Ocala, FL","event_type":"Equestrian / FEI show jumping","source_url":"https://worldequestriancenter.com/ocala-fl/equestrian/shows/november-december-show-series/","status":"Organizer-listed — confirm details","notes":"Public spectator event; confirm current access."},
]
for row in EQUINE:
    save_prospect(REP_EMAIL, row["segment"], row["name"], row["organization"], row["city"], row["state"],
                  row["contact_route"], row["source_url"], row["qualification_status"], row["permission_status"], row["notes"])
for event in STARTER_EVENTS:
    add_event(REP_EMAIL, **event)

st.title("🤝 Ashley’s Community Prospecting")
st.caption("Ocala equestrian relationships • shared team pipeline and event calendar")
st.info(
    "This workspace is for organization research, public professional routes, event planning, and opted-in contacts. "
    "Do not add patient, disability, diagnosis, support-group, or family data. Community programs are not prospect lists."
)

tabs = st.tabs(["Ocala Equine", "Shared Pipeline", "Request a List / Change", "Shared Events"])

def show_segment(segment: str, intro: str):
    st.write(intro)
    rows = list_prospects(segment=segment)
    df = pd.DataFrame(rows)
    if not df.empty:
        show = df[["name","organization","city","state","contact_route","source_url","qualification_status","permission_status","notes"]]
        st.dataframe(show, hide_index=True, width="stretch", column_config={"source_url":st.column_config.LinkColumn("Source")})
        st.download_button(f"Download {segment} organizations CSV", show.to_csv(index=False).encode("utf-8-sig"),
                           file_name=f"devin_{segment.lower().replace(' ','_')}_organizations.csv", mime="text/csv")
    st.caption("Organization records are research targets. Verify current roles, route, event rules, and firm requirements before outreach.")

with tabs[0]:
    show_segment("Ocala Equine",
        "Build from Devin’s existing relationships in the Ocala horse community. Begin with the Ocala CEP Equine Initiative, Ocala Horse Alliance, show organizers, and public equestrian events; prioritize introductions and service over event-floor prospecting.")
    st.markdown("**Current event anchors:** WEC’s November/December show series, HITS Post Time Dressage, the Arabian & Half Arabian Holiday Festival, and Florida Horse Park events. Verify the organizer listing before travel.")
with tabs[2]:
    st.write("Prospects entered here are shared with the main Command Center when both deployments use the same persistent database.")
    all_rows = list_prospects(limit=2000)
    if all_rows:
        df = pd.DataFrame(all_rows)
        st.dataframe(df[["created_at","rep_email","segment","name","organization","city","state","contact_route","source_url","qualification_status","permission_status"]], hide_index=True, width="stretch")
        st.download_button("Download shared pipeline CSV", df.to_csv(index=False).encode("utf-8-sig"), file_name="community_shared_pipeline.csv", mime="text/csv")
    else:
        st.caption("No shared prospects yet.")
    st.subheader("Upload a researched CSV into the shared pipeline")
    st.caption("Accepted fields include name, organization, city, state, contact_route, source_url, qualification_status, permission_status, and notes. Review and deduplicate before import.")
    uploaded = st.file_uploader("Choose CSV", type=["csv"], key="community_csv")
    segment = st.selectbox("Assign segment", ["Ocala Equine","Other Central Florida"])
    if uploaded and st.button("Add CSV rows to shared pipeline", type="primary"):
        try:
            parsed = pd.read_csv(uploaded).fillna("").to_dict(orient="records")
            added, skipped = import_csv_rows(REP_EMAIL, parsed, segment)
            st.success(f"Added {added} new rows; skipped {skipped} blank or duplicate rows.")
        except Exception as exc:
            st.error(f"Could not import this CSV: {exc}")
with tabs[3]:
    st.write("Submit a structured request for a new prospect list, event search, or experience change. Requests are saved in the shared queue and can be downloaded to bring into a research session.")
    with st.form("devin_request"):
        request_type = st.selectbox("Request type", ["New prospect list","Find events","Add industry / community","Change territory or filters","Tailor scripts / experience","App feature request","Other"])
        focus = st.selectbox("Focus", ["Ocala Equine","Other Central Florida"])
        territory = st.text_input("Territory", value="Central Florida / Ocala, FL")
        prompt = st.text_area("What should be researched or changed?", placeholder="Describe audience, geography, date range, source standards, and what would make the result useful.", height=140)
        submitted = st.form_submit_button("Submit request", type="primary")
    if submitted:
        if not prompt.strip():
            st.error("Describe the request first.")
        else:
            submit_request(REP_EMAIL, request_type, focus, territory, prompt.strip())
            st.success("Saved to the shared request queue.")
    requests = list_requests()
    if requests:
        reqdf = pd.DataFrame(requests)
        st.dataframe(reqdf[["created_at","rep_email","request_type","focus","territory","request_text","status"]], hide_index=True, width="stretch")
        st.download_button("Download request queue JSON", json.dumps(requests, indent=2), file_name="devin_research_requests.json", mime="application/json")
    st.caption("Requests are queued and downloadable. The app does not run a ChatGPT research agent automatically; research results can be uploaded above and will then appear in the shared pipeline.")
with tabs[4]:
    st.write("Events Devin adds here are stored in the shared calendar table and are also displayed on the main Command Center’s Event Schedule.")
    with st.form("devin_add_event"):
        title = st.text_input("Event name")
        organizer = st.text_input("Organizer")
        c1,c2,c3=st.columns(3)
        with c1: start_date = st.date_input("Start date", value=date.today(), format="YYYY-MM-DD")
        with c2: end_date = st.date_input("End date (same day if one-day event)", value=date.today(), format="YYYY-MM-DD")
        with c3: start_time = st.text_input("Time / time range", value="Confirm with organizer")
        location = st.text_input("Location")
        event_type = st.selectbox("Event type", ["Equestrian","Business networking","Community / charity","Other"])
        source_url = st.text_input("Public source URL")
        notes = st.text_area("Verification / attendance notes")
        add_submitted = st.form_submit_button("Add to shared event calendar", type="primary")
    if add_submitted:
        if not title.strip():
            st.error("Enter an event name.")
        elif end_date < start_date:
            st.error("End date must be on or after start date.")
        else:
            result = add_event(REP_EMAIL, title.strip(), organizer.strip(), start_date.isoformat(), end_date.isoformat(),
                               start_time.strip(), location.strip(), event_type, source_url.strip(), notes.strip())
            st.success("Added to the shared calendar." if result else "That event already exists in the shared calendar.")
    event_rows = list_events()
    if event_rows:
        edf = pd.DataFrame(event_rows)
        st.dataframe(edf[["start_date","end_date","start_time","title","organizer","location","event_type","status","source_url","rep_email"]], hide_index=True, width="stretch", column_config={"source_url":st.column_config.LinkColumn("Source")})
        st.download_button("Download shared events CSV", edf.to_csv(index=False).encode("utf-8-sig"), file_name="community_shared_events.csv", mime="text/csv")
