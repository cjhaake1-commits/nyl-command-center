from __future__ import annotations

from datetime import date
import streamlit as st

from core.rep_profile import REP_NAME

st.set_page_config(page_title="Veterinary Clinics", page_icon="🐾", layout="wide")

st.title("Veterinary Clinics")
st.caption("Devin’s Central Florida relationship-development lane")
st.info(
    "Start with Devin’s existing professional relationships and ask where a useful introduction or conversation would be welcome. "
    "Clinic names below are public research candidates, not validated leads or evidence of financial need."
)

st.subheader("Conversation approach")
st.markdown("""
- Begin with Devin’s veterinary-clinic experience and familiarity with the day-to-day realities of practice ownership and team life.
- Ask what topics are useful to the clinic: employee benefits education, owner protection planning, retention, or business continuity.
- Respect clinical schedules; request a brief introduction or an appropriate meeting time rather than pitching during patient-care hours.
- Avoid collecting employee or owner health, compensation, or financial details in prospect notes. Do not suggest a product is appropriate before a proper fact-finding and suitability process.
""")

st.subheader("Central Florida clinic research candidates")
st.caption(f"Public directory leads reviewed {date.today().isoformat()}. Verify current ownership, location, services, and contact details directly before outreach.")
clinics = [
    ("Winter Park Veterinary Hospital", "Winter Park; family-owned clinic serving Winter Park, Maitland, College Park and greater Orlando.", "https://wpvet.com/"),
    ("Animal Hospital at Lake Baldwin Park", "Orlando; general practice with boarding, exotics and specialty services (directory listing).", "https://petallianceorlando.org/veterinary-care/emergencies/"),
    ("Corrine Drive Animal Hospital", "Orlando; neighborhood clinic with specialist referrals listed in the Pet Alliance directory.", "https://petallianceorlando.org/veterinary-care/emergencies/"),
    ("Lake Nona Animal Clinic", "East Orlando; primary-care clinic listed in the Pet Alliance directory.", "https://petallianceorlando.org/veterinary-care/emergencies/"),
    ("Waterford Lakes Animal Hospital", "East Orlando; full-service clinic listing in the Pet Alliance directory.", "https://petallianceorlando.org/veterinary-care/emergencies/"),
    ("Alafaya Trail Animal Hospital", "Oviedo; clinic listing includes boarding and bathing services.", "https://petallianceorlando.org/veterinary-care/emergencies/"),
    ("Longwood Veterinary Clinic", "Longwood; general practice listed in the Pet Alliance directory.", "https://petallianceorlando.org/veterinary-care/emergencies/"),
    ("Luv-N-Care Animal Hospital", "Longwood; directory lists a broad range of services including exotics and boarding.", "https://petallianceorlando.org/veterinary-care/emergencies/"),
    ("Veterinary Emergency Clinic of Central Florida", "Emergency and urgent-care network with locations in Casselberry, Waterford Lakes, Oakland and The Villages.", "https://veconline.com/locations/"),
    ("BluePearl Pet Hospital Orlando", "Maitland specialty and emergency hospital serving greater Orlando; specialty visits commonly come through referring veterinarians.", "https://bluepearlvet.com/hospital/maitland-Fl/"),
]
for name, details, url in clinics:
    with st.expander(name):
        st.write(details)
        st.link_button("Review public clinic information", url)

st.subheader("Practice and referral network")
st.markdown("""
- **Practice decision-makers:** practice owners, managing veterinarians, hospital administrators, and practice managers.
- **Professional network:** Florida Veterinary Medical Association (FVMA), local veterinary groups, practice consultants, payroll/benefits administrators, CPAs, commercial bankers, and business attorneys.
- **Potential educational topics:** employee benefits basics; protecting a practice owner’s family and business continuity; planning for a future ownership transition; financial-wellness education for veterinary teams.
- **Event channel:** FVMA conferences and CE events bring together veterinarians and the wider veterinary team. Monitor the official calendar and add only future, confirmed events to the shared calendar.
""")

st.subheader("Events to monitor")
events = [
    ("Florida Veterinary Medical Association (FVMA) conferences", "Official calendar for annual conference, regional CE and team events. The listed 2026 annual conference dates have passed; check for newly announced future events before scheduling.", "https://fvma.org/conferences/"),
    ("Fun in the Sun Grooming Show", "Orlando pet-care industry event with professional attendance rules; verify organizer’s next dates and attendee eligibility.", "https://www.fitsgroom.com/attend"),
    ("University of Florida veterinary continuing education", "Monitor UF College of Veterinary Medicine events and CE notices for Central Florida opportunities.", "https://vetmed.ufl.edu/education/continuing-education/"),
]
for title, detail, url in events:
    st.markdown(f"**{title}**  \n{detail}  \n[Check organizer’s current calendar]({url})")

st.subheader("Add an office from Devin’s own network")
st.caption("Add a clinic she knows directly. Saving creates a Veterinary Clinic record in the Command Center prospect pipeline.")
from data.prospects import add_prospect, get_prospects, init_prospect_db
init_prospect_db()

with st.form("add_veterinary_clinic"):
    clinic_name = st.text_input("Clinic / office name *")
    city = st.text_input("City / area", placeholder="e.g., Winter Park")
    contact_name = st.text_input("Known contact (optional)")
    role = st.text_input("Role (optional)", placeholder="Practice manager, veterinarian, owner")
    public_contact = st.text_input("Business phone or email (optional)")
    relationship = st.selectbox(
        "How Devin knows the office",
        ["Existing professional relationship", "Warm introduction", "Former colleague / workplace", "Public business research", "Other"],
    )
    source_detail = st.text_input("Source or introduction path (optional)")
    next_action = st.text_input("Suggested next step", value="Ask permission for a brief business conversation")
    office_notes = st.text_area("Business context only — no employee health, compensation, or private financial details")
    submitted = st.form_submit_button("Add clinic to prospect pipeline", type="primary")

if submitted:
    if not clinic_name.strip():
        st.error("Enter the clinic or office name.")
    else:
        known = get_prospects()
        duplicate = any(
            str(p.get("organization", "")).strip().casefold() == clinic_name.strip().casefold()
            and str(p.get("market_segment", "")).casefold() == "veterinary clinic"
            for p in known
        )
        if duplicate:
            st.warning("That clinic is already in the prospect pipeline.")
        else:
            details = " | ".join(x for x in [city.strip(), role.strip(), public_contact.strip()] if x)
            if contact_name.strip():
                details = f"{contact_name.strip()} — {details}" if details else contact_name.strip()
            if source_detail.strip():
                details = f"{details} | Relationship/source: {source_detail.strip()}" if details else source_detail.strip()
            add_prospect(
                prospect_name=contact_name.strip() or clinic_name.strip(),
                organization=clinic_name.strip(),
                market_segment="Veterinary Clinic",
                source=relationship,
                source_detail=details,
                stage="New",
                fit_score=3,
                warmth_score=4 if relationship in {"Existing professional relationship", "Warm introduction", "Former colleague / workplace"} else 2,
                urgency_score=3,
                source_quality=4 if public_contact.strip() else 3,
                consent_status="Existing relationship" if relationship in {"Existing professional relationship", "Former colleague / workplace"} else "Unknown",
                next_action=next_action.strip(),
                next_action_date=str(date.today()),
                notes=office_notes.strip(),
            )
            st.success("Clinic added to the Command Center prospect pipeline.")
            st.rerun()

clinic_pipeline = [
    p for p in get_prospects()
    if str(p.get("market_segment", "")).casefold() == "veterinary clinic"
]
if clinic_pipeline:
    st.markdown("#### Devin’s saved veterinary offices")
    st.dataframe(
        [{
            "Clinic": p.get("organization", ""),
            "Contact": p.get("prospect_name", ""),
            "Stage": p.get("stage", ""),
            "Next step": p.get("next_action", ""),
            "Due": p.get("next_action_date", ""),
            "Relationship/source": p.get("source", ""),
        } for p in clinic_pipeline],
        width="stretch",
        hide_index=True,
    )

st.subheader("Suggested next steps")
st.markdown("""
1. Have Devin map her existing clinic relationships by clinic, role, relationship warmth, and the best permission-based introduction.
2. Prioritize a small number of warm introductions before cold outreach; confirm the recipient’s role and the clinic’s current ownership.
3. Offer a short educational conversation tailored to the clinic’s stated interest, with NYL-approved materials and supervisory review.
4. Log organization, public business contact, source URL, relationship path, permission, and dated next action in the prospect pipeline.
5. Review the FVMA and clinic calendars monthly; add verified events to the shared calendar with an attendance purpose and registration link.
""")
st.caption(f"Prepared for {REP_NAME} • Business-development research only. Confirm current NYL product, licensing, suitability, and advertising requirements before client-facing discussions.")
