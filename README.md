# NYL Command Center

A standalone goal-to-action operating system for a New York Life sales career.

## What is live now

### Daily War Room

The UI now turns a commission goal and deadline into an exact execution mission:

- configurable commission goal and deadline
- selectable selling days
- execution buffer above the mathematical minimum
- Gate / 1.25x / 1.5x / 2x / 3x record modes
- today's required commission, sales, held appointments, booked appointments, conversations, and outreach
- this week's required production
- automatic recalculation after actual results are logged
- adaptive funnel assumptions that blend real performance with starting assumptions
- weakest-link detection across contact, booking, show, close, and average-commission stages
- record-setting scenario table
- daily activity history and CSV export

The starting **$3,000 / 30-day commission gate** remains the default, but any target can be entered.

All funnel assumptions are editable. The initial defaults are placeholders, not New York Life compensation facts.

## Isolation rules

This repository is intentionally separate from every other project. Keep its virtual environment, secrets, database, and deployment independent.

- Use a dedicated `.venv` inside this repository.
- Keep local secrets in `.env`; `.env` is ignored by Git.
- The SQLite database stays local and is ignored by Git.
- Do not copy configuration or credentials from unrelated projects.
- Deploy this repository independently from other systems.

## View the UI on your computer

### Option A — GitHub Desktop

1. In GitHub Desktop, clone `cjhaake1-commits/nyl-command-center` into its own local folder.
2. Open that folder in VS Code.
3. Open the VS Code terminal.
4. Run the commands for your operating system below.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

### Mac / Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Streamlit will print a local address, normally:

```text
http://localhost:8501
```

Open that address in your browser. Leave the terminal running while you use the Command Center.

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

Example starting assumptions:

- Goal: $3,000
- Average commission per placed sale: $750
- Held appointment close rate: 30%
- Appointment show rate: 75%
- Conversation-to-booking rate: 25%
- Outreach-to-conversation rate: 30%

Those defaults produce a planning estimate of about 4 placed sales, 14 held appointments, 19 booked appointments, 76 conversations and 254 outreach attempts across a 30-day period when all 30 days are treated as active selling days. The Daily War Room now lets you choose the actual weekdays you intend to sell and recalculates the daily burden accordingly.

## Adaptive planning

Once real activity is logged, the War Room begins blending your actual performance with the starting assumptions. This avoids replacing the model with one lucky or unlucky day while still allowing the plan to become increasingly personal to your real conversion rates and average commission.

## Compliance boundary

This is intentionally a **personal productivity and performance system**, not a client system of record.

Do not store sensitive client information such as Social Security numbers, account numbers, medical information, or other protected/sensitive data here. Product-specific recommendations and regulated communications should stay inside New York Life-approved systems and compliance workflows.

## Next build phases

### Phase 3 — Prospect Pipeline
- non-sensitive prospect tracking
- referral source analytics
- stage conversion analytics
- next-action dates
- priority scoring
- follow-up queue

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
