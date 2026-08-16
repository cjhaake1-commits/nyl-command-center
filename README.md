# NYL Command Center

A standalone goal-to-action operating system for a New York Life sales career.

## Current MVP

- Starts with a configurable **$3,000 / 30-day commission gate**.
- Works backward from commission goal to:
  - placed sales
  - held appointments
  - booked appointments
  - conversations
  - outreach attempts
- Converts remaining production into a daily minimum pace.
- Tracks actual activity and commission in SQLite.
- Shows pace versus goal.
- Includes 1.5x, 2x and 3x "record-setting" scenarios.
- Exports activity history to CSV.

All funnel assumptions are editable. The initial defaults are placeholders, not New York Life compensation facts.

## Isolation rules

This repository is intentionally separate from every other project. Keep its virtual environment, secrets, database, and deployment independent.

- Use a dedicated `.venv` inside this repository.
- Keep local secrets in `.env`; `.env` is ignored by Git.
- The SQLite database lives under `data/` and is ignored by Git.
- Do not copy configuration or credentials from unrelated projects.
- Deploy this repository independently from other systems.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## First 30-day logic

The engine uses this funnel:

```text
outreach attempts
  -> conversations
  -> appointments booked
  -> appointments held
  -> placed sales
  -> commission
```

For each step, the system uses an editable conversion assumption. It then calculates the activity needed to hit the goal.

Example default assumptions:

- Goal: $3,000
- Average commission per placed sale: $750
- Held appointment close rate: 30%
- Appointment show rate: 75%
- Conversation-to-booking rate: 25%
- Outreach-to-conversation rate: 30%

Those defaults produce a planning estimate of about 4 placed sales, 14 held appointments, 19 booked appointments, 76 conversations and 254 outreach attempts across the goal period.

## Compliance boundary for MVP

This is intentionally a **personal productivity and performance system**, not a client system of record.

Do not store sensitive client information such as Social Security numbers, account numbers, medical information, or other protected/sensitive data in this MVP. Product-specific recommendations and regulated communications should stay inside New York Life-approved systems and compliance workflows.

## Recommended next build phases

### Phase 2 — Daily War Room
- automatic morning plan
- weekly target allocator
- backlog / follow-up queue
- "what do I do next?" priority engine
- streaks and pace alerts

### Phase 3 — Prospect Pipeline
- non-sensitive prospect tracking
- referral source analytics
- stage conversion analytics
- next-action dates
- priority scoring

### Phase 4 — AI Coach
- generates daily plan from actual performance
- diagnoses weakest conversion step
- proposes experiments
- meeting-prep templates
- draft outreach for human review

### Phase 5 — Income Stack
- insurance commissions
- renewals / persistency
- securities revenue
- advisory revenue
- management economics
- multi-year income forecasting

### Phase 6 — Record Book
- personal bests
- weekly/monthly records
- production leaderboard against self-defined benchmarks
- stretch-goal simulator
