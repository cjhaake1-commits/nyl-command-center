from core.planner import FunnelAssumptions, build_plan, pace_status


def test_default_3000_plan():
    p = build_plan(3000, 0, 30, FunnelAssumptions())
    assert p.sales_needed == 4
    assert p.held_appointments_needed == 14
    assert p.booked_appointments_needed == 19
    assert p.conversations_needed == 76
    assert p.outreach_attempts_needed == 254


def test_partial_progress():
    p = build_plan(3000, 1500, 10, FunnelAssumptions(avg_commission_per_sale=750))
    assert p.remaining_commission == 1500
    assert p.sales_needed == 2


def test_pace():
    result = pace_status(3000, 1000, 10, 30)
    assert result["status"] == "on pace"
