from __future__ import annotations

from datetime import date

ACCOUNT_SCORE_DIMENSIONS = [
    {
        "key": "need_score",
        "label": "Need signal",
        "levels": {
            0: "No relevant signal",
            1: "Generic fit only",
            2: "One visible issue or growth trigger",
            3: "Multiple credible triggers or adviser-confirmed issue",
        },
    },
    {
        "key": "access_score",
        "label": "Access",
        "levels": {
            0: "No path",
            1: "Cold role/company only",
            2: "Event, shared group, or known COI path",
            3: "Direct introduction or active conversation",
        },
    },
    {
        "key": "strategic_fit_score",
        "label": "Economic / strategic fit",
        "levels": {
            0: "Outside niche",
            1: "Small or transactional fit",
            2: "Meaningful owner/executive planning potential",
            3: "Complex multi-issue relationship and specialist leverage",
        },
    },
    {
        "key": "timing_score",
        "label": "Timing",
        "levels": {
            0: "No timing",
            1: "Long-term nurture",
            2: "Event or change within 12 months",
            3: "Active decision, transaction, renewal, succession, or expansion",
        },
    },
]

FIRST_100_COMPOSITION = [
    {
        "segment": "Owner-led growth companies",
        "target": 40,
        "why": "Highest fit for continuity, key-person, ownership, retention, and owner-planning conversations.",
        "access": "ACG, chambers, expansion news, commercial COIs",
    },
    {
        "segment": "Medical / professional practice owners",
        "target": 20,
        "why": "Owner income, partner structure, disability, retention, retirement, and personal planning.",
        "access": "Practice associations, CPAs, attorneys, bankers",
    },
    {
        "segment": "Centers of influence",
        "target": 20,
        "why": "Credibility and repeatable introductions into real planning events.",
        "access": "Direct research, ACG, estate-planning and banking networks",
    },
    {
        "segment": "Hospitality / construction / real-estate operators",
        "target": 10,
        "why": "Large local ecosystems with executive, ownership, and key-person questions.",
        "access": "CFHLA, CREDA/NAIOP, GOBA and local business groups",
    },
    {
        "segment": "Established executives / technical professionals",
        "target": 10,
        "why": "Personal planning and introduction potential around growth employers and professional networks.",
        "access": "OEP, NeoCity, Lake Nona and professional events",
    },
]

PIPELINE_STAGES = [
    {
        "stage": "Target",
        "input": "Public companies, roles, COIs, event lists",
        "human_decision": "Does it meet the ICP?",
        "automation": "Saved searches, public alerts, approved list import",
        "exit": "Tier A/B/C and owner assigned",
    },
    {
        "stage": "Trigger",
        "input": "Growth, hiring, succession, transaction, expansion, event",
        "human_decision": "Is there a timely reason to speak?",
        "automation": "Alerts and research queue",
        "exit": "Source-backed trigger recorded",
    },
    {
        "stage": "Personalize",
        "input": "Company facts + one hypothesis",
        "human_decision": "Is the message relevant and accurate?",
        "automation": "AI draft from public data; human verification",
        "exit": "Approved one-sentence relevance",
    },
    {
        "stage": "Touch",
        "input": "Phone, email, LinkedIn, event",
        "human_decision": "Which channel best fits access?",
        "automation": "CRM task sequence and reminders",
        "exit": "Reply, live conversation, or recycle",
    },
    {
        "stage": "Meet",
        "input": "20-minute owner or COI conversation",
        "human_decision": "Is there a real issue and reason to continue?",
        "automation": "Scheduling and meeting brief",
        "exit": "Diagnostic scheduled or closed",
    },
    {
        "stage": "Diagnose",
        "input": "Facts, stakeholders, existing advisers, priorities",
        "human_decision": "Is there a material, addressable need?",
        "automation": "Structured fact-find; specialist handoff",
        "exit": "Agreed problem and next decision",
    },
    {
        "stage": "Design",
        "input": "Verified facts and options",
        "human_decision": "Which paths are appropriate and explainable?",
        "automation": "Advanced Planning / field consultants",
        "exit": "Recommendation meeting scheduled",
    },
    {
        "stage": "Implement",
        "input": "Decision, application, underwriting, documentation",
        "human_decision": "Does the client understand tradeoffs and affordability?",
        "automation": "Case management and follow-up tasks",
        "exit": "Delivered / implemented relationship",
    },
    {
        "stage": "Compound",
        "input": "Service milestone and review calendar",
        "human_decision": "Has value been delivered?",
        "automation": "7-day, 30-day, 90-day and annual review reminders",
        "exit": "Introductions and next planning issue",
    },
]

TOUCH_SEQUENCES = {
    "Owner 14-Day": [
        ("Day 0", "Research", "Verify one public trigger, score account, identify role", "Not enough evidence / wrong ICP"),
        ("Day 1", "Email", "Short trigger-based email and 20-minute ask", "Reply / DNC / wrong person"),
        ("Day 2", "Phone", "Concise call with one owner-level question", "Reply / DNC / wrong person"),
        ("Day 4", "LinkedIn", "Contextual connection or engagement if approved", "Reply / DNC"),
        ("Day 6", "Email", "Approved checklist or relevant event", "Reply / DNC"),
        ("Day 9", "Phone", "Second call / voicemail tied to issue", "Reply / DNC"),
        ("Day 14", "Email", "Close-loop / permission message", "Close / recycle"),
        ("Day 45+", "Research", "Recycle only with a new trigger", "Second cycle fails"),
    ],
    "COI 20-Day": [
        ("Day 0", "Research", "Understand niche, clients, and boundaries", "No complementarity"),
        ("Day 1", "Email", "Request 20-minute professional conversation", "Reply / DNC"),
        ("Day 3", "Phone", "Confirm relevance and propose two times", "Reply / DNC"),
        ("Day 7", "LinkedIn/Event", "Engage with real insight", "Reply / DNC"),
        ("Day 12", "Value Share", "Approved checklist, case theme, or co-host idea", "Reply / DNC"),
        ("Day 20", "Small Test", "One joint session or relevant introduction", "No interest"),
    ],
    "Event 10-Day": [
        ("At Event", "Conversation", "Capture exact topic and agreed follow-up", "No follow-up reason"),
        ("Within 24h", "Email", "Specific note and two time options", "Reply / DNC"),
        ("Day 3", "Phone/LinkedIn", "Ask one follow-up question", "Reply / DNC"),
        ("Day 7", "Value Share", "Approved resource or invitation", "Reply / DNC"),
        ("Day 10", "Close Loop", "Schedule or close", "Closed"),
    ],
}

WEEKLY_TARGETS = {
    "new_qualified_accounts": 18,
    "personalized_touches": 60,
    "meaningful_conversations": 11,
    "first_meetings": 4,
    "diagnostics": 2,
    "coi_meetings": 2,
    "introduction_asks": 5,
    "open_loops_closed_pct": 100,
}

HEALTHY_CONVERSION_RANGES = [
    ("Touch → meaningful conversation", 0.15, 0.25, "Improve list quality, trigger relevance, channel, and opening."),
    ("Conversation → first meeting", 0.25, 0.40, "Sharpen the reason to meet and use two specific time choices."),
    ("First meeting → diagnostic", 0.30, 0.50, "Improve questions, target seniority, and next-step close."),
    ("Event contact → meeting", 0.10, 0.20, "Prepare targets and send specific 24-hour follow-up."),
]

DAILY_TIME_BLOCKS = [
    ("7:45-8:15", "Dashboard and priority review", "Top 10 calls, meetings, overdue next steps, compliance issues"),
    ("8:15-9:00", "Research and personalization", "3 Tier A briefs; 5 verified triggers; messages ready"),
    ("9:00-11:00", "Outbound power block", "12-15 calls; 6-8 emails/DMs; protect the block"),
    ("11:00-12:00", "COI / introduction block", "2 COI touches; 1 introduction ask; event follow-up"),
    ("12:00-1:00", "Lunch / local visibility", "One lunch meeting or focused admin"),
    ("1:00-4:00", "First meetings, diagnostics, case work", "1-3 meaningful client/prospect interactions"),
    ("4:00-4:30", "Same-day follow-up", "Every meeting recap sent; next meeting requested"),
    ("4:30-5:00", "CRM closeout", "No active record left without a next date"),
]

FIRST_SALE_SPRINT = [
    {
        "week": "1 - Foundation",
        "build": "100 accounts; 20 Tier A; 20 COIs; approved scripts; booking process",
        "target": "15-20 touches by day four; 4 live conversations; 3 meetings booked",
        "objective": "Identify the strongest first issue and access path",
    },
    {
        "week": "2 - Conversation",
        "build": "Research next 20 accounts; attend one event",
        "target": "60 touches; 10 conversations; 3 first meetings; 1 COI meeting",
        "objective": "Advance one owner into a diagnostic",
    },
    {
        "week": "3 - Diagnosis",
        "build": "Prepare fact-find and specialist support",
        "target": "60 touches; 10 conversations; 3 first meetings; 1-2 diagnostics",
        "objective": "Define one material issue, stakeholders, and decision path",
    },
    {
        "week": "4 - Recommendation / implementation",
        "build": "Case design, comparison, underwriting preparation",
        "target": "60 touches; 3 first meetings; diagnostics; decision meetings",
        "objective": "Seek appropriate implementations only when genuinely ready",
    },
]

TWELVE_WEEK_PLAN = [
    (1, "Approvals, CRM, scorecard, 100 accounts, scripts", "15-20 touches; 3 meetings booked", "Is the environment approved and usable?"),
    (2, "Owner sequence batch 1; COI batch 1", "60 touches; 3 first meetings; 1 COI meeting", "Which opening earns dialogue?"),
    (3, "Owner sequence batch 2; first workshop outline", "60 touches; 3 meetings; 1-2 diagnostics", "Which issue earns a second meeting?"),
    (4, "Close loops; first case design; day-30 review", "60 touches; appropriate implementations only", "Retain only two acquisition channels."),
    (5, "Deepen winning niche; 20 new accounts", "60 touches; 3-4 meetings; 2 COI meetings", "Does niche conversion beat baseline?"),
    (6, "Run first owner workshop", "8-15 attendees; 2-3 follow-up diagnostics", "Is the event worth repeating?"),
    (7, "Build specialist and COI cadence", "60 touches; joint meetings; case progression", "Where does office support improve close speed?"),
    (8, "Second channel experiment", "60 touches; 3-4 meetings", "Scale or stop the second channel."),
    (9, "Client service and introduction system", "5 introduction asks; review tasks active", "Is value delivery generating access?"),
    (10, "Repeat winning workshop / roundtable", "Qualified attendees and meetings", "Can this become monthly?"),
    (11, "Analyze segment economics and time", "Conversion, case value, hours, costs", "Which segment deserves 60% of next-quarter capacity?"),
    (12, "Quarter review and Q2 plan", "Clean pipeline; 90-day forecast and calendar", "Specialize, simplify, and commit."),
]


def clamp_score(value: int | float | None) -> int:
    try:
        return max(0, min(3, int(value or 0)))
    except (TypeError, ValueError):
        return 0


def account_score(need: int, access: int, fit: int, timing: int) -> int:
    return sum(clamp_score(v) for v in (need, access, fit, timing))


def tier_for_score(score: int) -> str:
    score = max(0, min(12, int(score)))
    if score >= 9:
        return "A"
    if score >= 6:
        return "B"
    return "C"


def next_action_status(next_action_date: str | None, today: date | None = None) -> str:
    today = today or date.today()
    if not next_action_date:
        return "No next date"
    try:
        due = date.fromisoformat(str(next_action_date)[:10])
    except ValueError:
        return "Invalid date"
    if due < today:
        return "Overdue"
    if due == today:
        return "Due today"
    return "Scheduled"
