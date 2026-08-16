from datetime import date

from core.planner import FunnelAssumptions, build_plan
from core.war_room import adaptive_assumptions, build_daily_mission, count_selling_days, funnel_health, weakest_link


def test_count_selling_days_weekdays_only():
    assert count_selling_days(date(2026, 8, 17), date(2026, 8, 21), ["Mon", "Tue", "Wed", "Thu", "Fri"]) == 5


def test_daily_mission_adds_execution_buffer():
    plan = build_plan(3000, 0, 20, FunnelAssumptions())
    mission = build_daily_mission(plan, 1.10)
    assert mission.outreach_attempts >= 14
    assert mission.conversations >= 5


def test_adaptive_assumptions_uses_actuals_without_overreacting():
    totals = {
        "outreach_attempts": 100,
        "conversations": 40,
        "appointments_booked": 12,
        "appointments_held": 9,
        "sales": 4,
        "commission": 3600,
    }
    baseline = FunnelAssumptions()
    adaptive = adaptive_assumptions(totals, baseline)
    assert adaptive.contact_rate > baseline.contact_rate
    assert adaptive.avg_commission_per_sale > baseline.avg_commission_per_sale


def test_weakest_link_detects_underperforming_stage():
    totals = {
        "outreach_attempts": 100,
        "conversations": 10,
        "appointments_booked": 3,
        "appointments_held": 3,
        "sales": 1,
        "commission": 750,
    }
    baseline = FunnelAssumptions()
    weak = weakest_link(funnel_health(totals, baseline))
    assert weak is not None
    assert weak.stage == "Contact rate"
