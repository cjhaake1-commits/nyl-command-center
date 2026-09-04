from data.paul_market import (
    BUSINESS_TARGET_MET,
    HNW_LEADS,
    INDIVIDUAL_TARGET_MET,
    PUBLIC_LEADS,
)


def test_paul_targets_are_met():
    assert len(HNW_LEADS) >= 100
    assert len(PUBLIC_LEADS) >= 24
    assert INDIVIDUAL_TARGET_MET is True
    assert BUSINESS_TARGET_MET is True


def test_paul_rows_are_unique_and_isolated():
    names = [row['Name'].strip().casefold() for row in HNW_LEADS]
    businesses = [row['Business'].strip().casefold() for row in PUBLIC_LEADS]
    assert len(names) == len(set(names))
    assert len(businesses) == len(set(businesses))
    assert all(row['Tenant'] == 'Paul Beck' for row in HNW_LEADS + PUBLIC_LEADS)
    assert all('Simi Valley' in row['Territory'] for row in HNW_LEADS + PUBLIC_LEADS)


def test_paul_rows_are_research_hold_only():
    for row in HNW_LEADS + PUBLIC_LEADS:
        assert row['Outreach Status'] == 'HOLD'
        assert row['Research Status'] == 'RESEARCH ONLY'
        assert row['Compliance Status'] == 'COMPLIANCE REVIEW'


def test_no_central_florida_tenant_leakage():
    forbidden = ('chris haake', 'orlando', 'winter garden', 'central florida')
    for row in HNW_LEADS + PUBLIC_LEADS:
        searchable = ' '.join(str(value).casefold() for value in row.values())
        assert not any(term in searchable for term in forbidden)
