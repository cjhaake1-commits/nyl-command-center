from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import text

from data.db import engine


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def init_prospect_db() -> None:
    eng = engine()
    sqlite = eng.dialect.name == "sqlite"
    with eng.begin() as conn:
        if sqlite:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS prospects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prospect_name TEXT NOT NULL,
                    organization TEXT DEFAULT '',
                    market_segment TEXT DEFAULT 'Broad market',
                    source TEXT DEFAULT '',
                    source_detail TEXT DEFAULT '',
                    stage TEXT NOT NULL DEFAULT 'New',
                    fit_score INTEGER NOT NULL DEFAULT 3,
                    warmth_score INTEGER NOT NULL DEFAULT 3,
                    urgency_score INTEGER NOT NULL DEFAULT 3,
                    source_quality INTEGER NOT NULL DEFAULT 3,
                    consent_status TEXT DEFAULT 'Unknown',
                    next_action TEXT DEFAULT '',
                    next_action_date TEXT DEFAULT '',
                    last_contact_date TEXT DEFAULT '',
                    salesforce_record_id TEXT DEFAULT '',
                    crm_source TEXT DEFAULT 'Command Center',
                    do_not_contact INTEGER NOT NULL DEFAULT 0,
                    notes TEXT DEFAULT '',
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """))
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS prospect_touchpoints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prospect_id INTEGER NOT NULL,
                    external_id TEXT DEFAULT '',
                    source_system TEXT NOT NULL DEFAULT 'Command Center',
                    touch_type TEXT NOT NULL,
                    direction TEXT NOT NULL DEFAULT 'outbound',
                    occurred_at TEXT NOT NULL,
                    subject TEXT DEFAULT '',
                    summary TEXT DEFAULT '',
                    outcome TEXT DEFAULT '',
                    requires_follow_up INTEGER NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL,
                    UNIQUE(source_system, external_id)
                )
            """))
        else:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS prospects (
                    id BIGSERIAL PRIMARY KEY,
                    prospect_name TEXT NOT NULL,
                    organization TEXT DEFAULT '',
                    market_segment TEXT DEFAULT 'Broad market',
                    source TEXT DEFAULT '',
                    source_detail TEXT DEFAULT '',
                    stage TEXT NOT NULL DEFAULT 'New',
                    fit_score INTEGER NOT NULL DEFAULT 3,
                    warmth_score INTEGER NOT NULL DEFAULT 3,
                    urgency_score INTEGER NOT NULL DEFAULT 3,
                    source_quality INTEGER NOT NULL DEFAULT 3,
                    consent_status TEXT DEFAULT 'Unknown',
                    next_action TEXT DEFAULT '',
                    next_action_date VARCHAR(10) DEFAULT '',
                    last_contact_date VARCHAR(10) DEFAULT '',
                    salesforce_record_id TEXT DEFAULT '',
                    crm_source TEXT DEFAULT 'Command Center',
                    do_not_contact BOOLEAN NOT NULL DEFAULT FALSE,
                    notes TEXT DEFAULT '',
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """))
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS prospect_touchpoints (
                    id BIGSERIAL PRIMARY KEY,
                    prospect_id BIGINT NOT NULL,
                    external_id TEXT DEFAULT '',
                    source_system TEXT NOT NULL DEFAULT 'Command Center',
                    touch_type TEXT NOT NULL,
                    direction TEXT NOT NULL DEFAULT 'outbound',
                    occurred_at TEXT NOT NULL,
                    subject TEXT DEFAULT '',
                    summary TEXT DEFAULT '',
                    outcome TEXT DEFAULT '',
                    requires_follow_up BOOLEAN NOT NULL DEFAULT FALSE,
                    created_at TEXT NOT NULL,
                    UNIQUE(source_system, external_id)
                )
            """))


def add_prospect(**values) -> None:
    now = _now_iso()
    payload = {
        "prospect_name": str(values.get("prospect_name", "")).strip(),
        "organization": str(values.get("organization", "")).strip(),
        "market_segment": str(values.get("market_segment", "Broad market")),
        "source": str(values.get("source", "")),
        "source_detail": str(values.get("source_detail", "")).strip(),
        "stage": str(values.get("stage", "New")),
        "fit_score": int(values.get("fit_score", 3)),
        "warmth_score": int(values.get("warmth_score", 3)),
        "urgency_score": int(values.get("urgency_score", 3)),
        "source_quality": int(values.get("source_quality", 3)),
        "consent_status": str(values.get("consent_status", "Unknown")),
        "next_action": str(values.get("next_action", "")).strip(),
        "next_action_date": str(values.get("next_action_date", "")),
        "last_contact_date": str(values.get("last_contact_date", "")),
        "salesforce_record_id": str(values.get("salesforce_record_id", "")).strip(),
        "crm_source": str(values.get("crm_source", "Command Center")),
        "do_not_contact": bool(values.get("do_not_contact", False)),
        "notes": str(values.get("notes", "")).strip(),
        "created_at": now,
        "updated_at": now,
    }
    with engine().begin() as conn:
        conn.execute(text("""
            INSERT INTO prospects (
                prospect_name, organization, market_segment, source, source_detail, stage,
                fit_score, warmth_score, urgency_score, source_quality, consent_status,
                next_action, next_action_date, last_contact_date, salesforce_record_id,
                crm_source, do_not_contact, notes, created_at, updated_at
            ) VALUES (
                :prospect_name, :organization, :market_segment, :source, :source_detail, :stage,
                :fit_score, :warmth_score, :urgency_score, :source_quality, :consent_status,
                :next_action, :next_action_date, :last_contact_date, :salesforce_record_id,
                :crm_source, :do_not_contact, :notes, :created_at, :updated_at
            )
        """), payload)


def get_prospects() -> list[dict]:
    with engine().connect() as conn:
        rows = conn.execute(text("SELECT * FROM prospects ORDER BY updated_at DESC, id DESC")).mappings().all()
        return [dict(row) for row in rows]


def update_prospect(prospect_id: int, **values) -> None:
    payload = {
        "id": int(prospect_id),
        "stage": str(values.get("stage", "New")),
        "next_action": str(values.get("next_action", "")).strip(),
        "next_action_date": str(values.get("next_action_date", "")),
        "last_contact_date": str(values.get("last_contact_date", "")),
        "consent_status": str(values.get("consent_status", "Unknown")),
        "do_not_contact": bool(values.get("do_not_contact", False)),
        "notes": str(values.get("notes", "")).strip(),
        "updated_at": _now_iso(),
    }
    with engine().begin() as conn:
        conn.execute(text("""
            UPDATE prospects SET
                stage=:stage,
                next_action=:next_action,
                next_action_date=:next_action_date,
                last_contact_date=:last_contact_date,
                consent_status=:consent_status,
                do_not_contact=:do_not_contact,
                notes=:notes,
                updated_at=:updated_at
            WHERE id=:id
        """), payload)


def prospect_counts() -> dict:
    with engine().connect() as conn:
        row = conn.execute(text("""
            SELECT
                COUNT(*) AS total,
                COALESCE(SUM(CASE WHEN stage NOT IN ('Won','Lost') THEN 1 ELSE 0 END),0) AS active,
                COALESCE(SUM(CASE WHEN stage='Appointment set' THEN 1 ELSE 0 END),0) AS appointments_set,
                COALESCE(SUM(CASE WHEN stage='Won' THEN 1 ELSE 0 END),0) AS won
            FROM prospects
        """)).mappings().one()
        return dict(row)


def add_touchpoint(
    prospect_id: int,
    touch_type: str,
    direction: str,
    occurred_at: str,
    subject: str = "",
    summary: str = "",
    outcome: str = "",
    requires_follow_up: bool = False,
    source_system: str = "Command Center",
    external_id: str = "",
) -> bool:
    payload = {
        "prospect_id": int(prospect_id),
        "external_id": external_id.strip(),
        "source_system": source_system.strip() or "Command Center",
        "touch_type": touch_type,
        "direction": direction,
        "occurred_at": occurred_at,
        "subject": subject.strip(),
        "summary": summary.strip(),
        "outcome": outcome.strip(),
        "requires_follow_up": bool(requires_follow_up),
        "created_at": _now_iso(),
    }
    with engine().begin() as conn:
        if external_id.strip():
            existing = conn.execute(text("""
                SELECT 1 FROM prospect_touchpoints
                WHERE source_system=:source_system AND external_id=:external_id
            """), payload).first()
            if existing:
                return False
        conn.execute(text("""
            INSERT INTO prospect_touchpoints (
                prospect_id, external_id, source_system, touch_type, direction, occurred_at,
                subject, summary, outcome, requires_follow_up, created_at
            ) VALUES (
                :prospect_id, :external_id, :source_system, :touch_type, :direction, :occurred_at,
                :subject, :summary, :outcome, :requires_follow_up, :created_at
            )
        """), payload)
        contact_date = occurred_at[:10]
        next_action = "Follow up" if requires_follow_up else ""
        conn.execute(text("""
            UPDATE prospects SET
                last_contact_date=:contact_date,
                next_action=CASE WHEN :next_action <> '' THEN :next_action ELSE next_action END,
                updated_at=:updated_at
            WHERE id=:prospect_id
        """), {
            "contact_date": contact_date,
            "next_action": next_action,
            "updated_at": _now_iso(),
            "prospect_id": int(prospect_id),
        })
    return True


def get_touchpoints(prospect_id: int | None = None, limit: int = 200) -> list[dict]:
    with engine().connect() as conn:
        if prospect_id is None:
            rows = conn.execute(text("""
                SELECT t.*, p.prospect_name, p.organization
                FROM prospect_touchpoints t
                JOIN prospects p ON p.id=t.prospect_id
                ORDER BY t.occurred_at DESC, t.id DESC
                LIMIT :limit
            """), {"limit": int(limit)}).mappings().all()
        else:
            rows = conn.execute(text("""
                SELECT t.*, p.prospect_name, p.organization
                FROM prospect_touchpoints t
                JOIN prospects p ON p.id=t.prospect_id
                WHERE t.prospect_id=:prospect_id
                ORDER BY t.occurred_at DESC, t.id DESC
                LIMIT :limit
            """), {"prospect_id": int(prospect_id), "limit": int(limit)}).mappings().all()
        return [dict(row) for row in rows]


def touchpoint_stats() -> dict:
    with engine().connect() as conn:
        row = conn.execute(text("""
            SELECT
                COUNT(*) AS total_touches,
                COALESCE(SUM(CASE WHEN direction='inbound' THEN 1 ELSE 0 END),0) AS inbound,
                COALESCE(SUM(CASE WHEN direction='outbound' THEN 1 ELSE 0 END),0) AS outbound,
                COALESCE(SUM(CASE WHEN requires_follow_up THEN 1 ELSE 0 END),0) AS follow_ups
            FROM prospect_touchpoints
        """)).mappings().one()
        return dict(row)
