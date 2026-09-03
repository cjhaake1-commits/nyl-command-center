from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

# Paul Deck has an isolated local database on his Streamlit tenant. Do not read the
# Chris Haake DATABASE_URL secret from this branch; that would mix activity/prospect data.
SQLITE_PATH = Path(__file__).resolve().parent / "paul_deck_command_center.db"
_ENGINE: Engine | None = None


def engine() -> Engine:
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = create_engine(f"sqlite:///{SQLITE_PATH}", pool_pre_ping=True, future=True)
    return _ENGINE


def storage_backend() -> str:
    return "Paul Deck isolated SQLite"


def storage_error() -> str:
    return ""


def persistent_storage_enabled() -> bool:
    return False


def _using_sqlite() -> bool:
    return True


def init_db() -> None:
    with engine().begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS daily_activity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity_date TEXT NOT NULL UNIQUE,
                outreach_attempts INTEGER NOT NULL DEFAULT 0,
                conversations INTEGER NOT NULL DEFAULT 0,
                appointments_booked INTEGER NOT NULL DEFAULT 0,
                appointments_held INTEGER NOT NULL DEFAULT 0,
                sales INTEGER NOT NULL DEFAULT 0,
                commission REAL NOT NULL DEFAULT 0,
                notes TEXT DEFAULT ''
            )
        """))


def upsert_daily_activity(activity_date: str, outreach_attempts: int, conversations: int, appointments_booked: int, appointments_held: int, sales: int, commission: float, notes: str = "") -> None:
    init_db()
    values = {
        "activity_date": activity_date,
        "outreach_attempts": outreach_attempts,
        "conversations": conversations,
        "appointments_booked": appointments_booked,
        "appointments_held": appointments_held,
        "sales": sales,
        "commission": commission,
        "notes": notes,
    }
    with engine().begin() as conn:
        conn.execute(text("""
            INSERT INTO daily_activity (
                activity_date, outreach_attempts, conversations, appointments_booked,
                appointments_held, sales, commission, notes
            ) VALUES (
                :activity_date, :outreach_attempts, :conversations, :appointments_booked,
                :appointments_held, :sales, :commission, :notes
            )
            ON CONFLICT(activity_date) DO UPDATE SET
                outreach_attempts=excluded.outreach_attempts,
                conversations=excluded.conversations,
                appointments_booked=excluded.appointments_booked,
                appointments_held=excluded.appointments_held,
                sales=excluded.sales,
                commission=excluded.commission,
                notes=excluded.notes
        """), values)


def get_activity() -> list[dict]:
    init_db()
    with engine().connect() as conn:
        return [dict(row) for row in conn.execute(text("SELECT * FROM daily_activity ORDER BY activity_date ASC")).mappings().all()]


def totals() -> dict:
    init_db()
    with engine().connect() as conn:
        row = conn.execute(text("""
            SELECT
                COALESCE(SUM(outreach_attempts),0) AS outreach_attempts,
                COALESCE(SUM(conversations),0) AS conversations,
                COALESCE(SUM(appointments_booked),0) AS appointments_booked,
                COALESCE(SUM(appointments_held),0) AS appointments_held,
                COALESCE(SUM(sales),0) AS sales,
                COALESCE(SUM(commission),0) AS commission
            FROM daily_activity
        """)).mappings().one()
        return dict(row)
