from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

import data.db as db


def test_weekly_operating_plan_round_trip_and_update(monkeypatch):
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
    monkeypatch.setattr(db, "_ENGINE", test_engine)
    db.init_db()

    db.upsert_weekly_plan(
        "2026-10-19",
        20000.0,
        8,
        20,
        60,
        "Warm introductions",
        "Schedule qualified discovery meetings",
        "Confirm contract trigger and commission-credit rules",
        "Not reviewed",
    )
    saved = db.get_weekly_plan("2026-10-19")
    assert saved is not None
    assert saved["weekly_commission_target"] == 20000
    assert saved["held_appointment_target"] == 8
    assert saved["focus_lane"] == "Warm introductions"

    db.upsert_weekly_plan(
        "2026-10-19",
        22000.0,
        9,
        24,
        72,
        "Business owners and professional practices",
        "Develop one professional relationship",
        "No manager question queued",
        "Partially met",
    )
    updated = db.get_weekly_plan("2026-10-19")
    assert updated is not None
    assert updated["weekly_commission_target"] == 22000
    assert updated["held_appointment_target"] == 9
    assert updated["friday_review"] == "Partially met"
    test_engine.dispose()
