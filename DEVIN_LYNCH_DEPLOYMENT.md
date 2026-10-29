# Devin Lynch Command Center

Separate Streamlit entry point and branch, following the Paul Beck tenant pattern.

- Branch: `devin-lynch-central-florida`
- Entry point: `app_devin_lynch.py`
- App title: Devin Lynch Command Center
- User email: dbl1095@aol.com
- Initial focus: Central Florida special-needs community education and Ocala equestrian relationships

## Deployment requirements

Create a separate Streamlit app from this repository and branch, using `app_devin_lynch.py` as the main file. Set its sharing/authentication to private and allow only the intended user. Streamlit Cloud deployment and invite management must be completed in the Streamlit account UI.

Configure the same persistent `DATABASE_URL` used by the main Command Center. The community request queue, research records, and events use shared PostgreSQL tables. SQLite fallback storage is local to each app and will not synchronize the two deployments.

This tenant intentionally includes the existing Command Center pages and data sources to match the requested access. Devin's community prospects, requests, and events are identified by rep email; all added events appear in the main Event Schedule when both apps use the shared database.

## Request workflow

The Community Prospecting page stores requests and supports CSV downloads/imports. It does not call a hosted ChatGPT research agent by itself. To fulfill a request, research the request in the connected assistant workflow, prepare a reviewed CSV, then import it into the shared pipeline. Event additions are shared directly.

## Privacy and compliance

Keep the Streamlit deployment private. Do not put medical or disability details, patient/support-group information, or sensitive client data in this app. Community organizations and events are research/relationship routes, not permission to solicit. Verify current event details and obtain required New York Life/SMRU approval before outreach, sponsorship, or co-branded education.
