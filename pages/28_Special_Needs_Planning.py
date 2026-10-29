from __future__ import annotations

from datetime import date
import streamlit as st

from core.rep_profile import REP_NAME

st.set_page_config(page_title="Special Needs Planning", page_icon="💛", layout="wide")

st.title("Special Needs Planning")
st.caption("Devin’s cornerstone community initiative • Central Florida + Ocala")
st.info(
    "Lead with listening and community service. Devin can share her family’s lived experience and what she learned by participating in planning for her sister. "
    "Every family’s circumstances differ; never assume a need, solicit private health details, or imply a guaranteed outcome."
)

st.subheader("A compassionate way to open the conversation")
st.markdown(
    "> “My sister has a disability, and I’ve seen firsthand how much thought goes into planning for the future. "
    "I’m learning from families and local organizations about what support is useful. If it would ever help, I can share what I learned and connect you with the right professionals.”"
)
st.caption("Ask permission before discussing finances. Let the family set the pace. Offer a useful resource or introduction even when no planning conversation follows.")

st.subheader("New York Life resources • quick reference")
st.markdown("""
- **Special-needs financial planning:** NYL’s public overview discusses benefit coordination, first-party and third-party special-needs trusts, ABLE accounts, letters of intent, guardianship, wills, and periodic plan reviews. [Read the overview](https://www.newyorklife.com/articles/special-needs-financial-planning)
- **Life insurance and planning:** NYL explains how a parent’s coverage may be considered as one potential way to provide resources for a loved one, including where a properly drafted trust is intended to receive proceeds. Coverage is subject to underwriting and policy terms. [Read NYL’s overview](https://www.newyorklife.com/articles/life-insurance-for-disabled-individuals)
- **Estate-planning guidance:** NYL describes identifying potential planning needs and coordinating with a client’s other advisors. For legal documents, trust design, benefit eligibility, and tax questions, refer the family to qualified attorneys and tax professionals. [NYL estate-planning page](https://www.newyorklife.com/products/advisory-services/estate-planning)
- **Caregiver checklist:** A short NYL Group Benefit Solutions handout suggests organizing care records and considering future financial needs. [Download the caregiver guide (PDF)](https://www.newyorklife.com/assets/gbs/pdf/Tips-For-Special-Needs-Caregivers.pdf)
- **Important boundary:** These are educational starting points, not a promise that a specific product is available or suitable. Confirm current NYL product, underwriting, licensing, and supervisory requirements before discussing a solution.
""")

st.subheader("Central Florida relationship map")
orgs = [
    ("Autism Society of Greater Orlando (ASGO)", "Parent-led Central Florida autism organization; family events, volunteer and participation opportunities.", "https://www.asgo.org/"),
    ("UCF Center for Autism and Related Disabilities (UCF-CARD)", "Family support, training, public awareness partnerships. Ask about agency presentations and approved community events.", "https://ucf-card.org/"),
    ("Down Syndrome Association of Central Florida (DSACF)", "Programs and events for individuals and families across life stages; review event guidelines and volunteer opportunities.", "https://dsacf.org/"),
    ("Special Olympics Florida • Central Region", "Athlete programs, community engagement and public events; connect through the regional team.", "https://www.specialolympicsflorida.org/central"),
    ("PALS / Orange County Safety Day", "Sensory-aware community safety education and resource fair for people on the spectrum and caregivers.", "https://flpals.org/events/safety-day/"),
    ("Ocala Therapeutic Recreation", "City programs designed for people with disabilities, including inclusive recreation and volunteer opportunities.", "https://www.ocalafl.gov/government/city-departments-i-z/recreation-parks/recreation/therapeutic-recreation"),
    ("Champions for Champions (Ocala)", "Local educational, sports, music and life-skills programming for people with special needs.", "https://championsforchampions.org/"),
    ("Center for Independent Living of North Central Florida", "Independent living and inclusion resources; explore community partnerships and educational events.", "https://www.cilncf.org/"),
]
for name, desc, url in orgs:
    with st.expander(name):
        st.write(desc)
        st.link_button("Organization site", url)

st.subheader("Events and participation")
st.caption(f"Last reviewed: {date.today().isoformat()}. Event dates and registration can change; confirm details with the organizer before adding an event to the shared calendar.")
events = [
    ("Special Olympics Florida event calendar", "Current statewide schedule; check Orlando-area competitions, family webinars and fundraising events. Ask organizers whether an event is open to the public or sponsorship-only.", "https://www.specialolympicsflorida.org/events"),
    ("DSACF events calendar", "Family programs, walks, caregiver gatherings and community events. Follow event-specific participation guidance.", "https://dsacf.org/events/list/"),
    ("UCF-CARD calendar and public awareness", "Training, family resources and community partnership opportunities; email ucfcard@ucf.edu to request presence at an awareness event or a brief agency presentation.", "https://ucf-card.org/what-we-do/"),
    ("PALS Safety Day", "Annual inclusive safety and resource event in Orlando; the organizer’s page lists current date, registration and sponsorship details.", "https://flpals.org/events/safety-day/"),
    ("Ocala Therapeutic Recreation calendar", "City-run adaptive recreation; dates, registration requirements, fees and volunteer availability are listed by program.", "https://www.ocalafl.gov/government/city-departments-i-z/recreation-parks/recreation/therapeutic-recreation"),
]
for title, desc, url in events:
    st.markdown(f"**{title}**  \n{desc}  \n[Check current details]({url})")

st.subheader("A respectful outreach rhythm")
st.markdown("""
1. **Show up first:** Attend public programs as a community member or volunteer, following organizer rules. Ask before requesting a speaking role or distributing materials.
2. **Build with the organization:** Offer a short, no-pressure educational session only when invited and approved. Make the topic practical (future-care planning questions and professional team coordination), not product-centered.
3. **Invite opt-in conversations:** Let families ask for a follow-up. Do not collect diagnoses, benefit status, or family-care details in prospect notes.
4. **Track only appropriate business context:** Record the organization, public event, relationship contact, permission granted, and next step. Keep sensitive health and benefit information out of the prospect pipeline.
5. **Coordinate before presenting:** Review any public materials or seminar content through NYL supervision/compliance and use approved disclosures.
""")

st.subheader("Prospecting targets for Devin")
st.markdown("""
- **Organizations:** disability-serving nonprofits, caregiver groups, adaptive recreation programs, parent-led associations, transition and independent-living organizations.
- **Centers of influence:** estate-planning attorneys, special-needs trust attorneys, elder-law attorneys, CPAs, care managers, benefits counselors, social workers, and fiduciaries. Build referral relationships without implying legal or benefits expertise.
- **Event plan:** add verified public events to the shared event calendar; note organizer, registration/contact link, attendance or volunteer purpose, and follow-up date.
- **Review cadence:** revisit organization calendars monthly and confirm each event directly before attending or inviting anyone.
""")
st.caption(f"Prepared for {REP_NAME} • Community education and relationship development only. Follow NYL policies and applicable privacy, licensing, and advertising rules.")
