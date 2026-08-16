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
