from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def test_every_registered_navigation_target_exists():
    app_source = (ROOT / "app.py").read_text(encoding="utf-8")
    page_paths = re.findall(r'st\.Page\(["\']([^"\']+)["\']', app_source)
    assert page_paths, "No Streamlit pages were registered in app.py"
    missing = [page for page in page_paths if not (ROOT / page).is_file()]
    assert not missing, f"Registered navigation page(s) missing: {missing}"


def test_core_workflow_pages_are_registered_in_navigation():
    app_source = (ROOT / "app.py").read_text(encoding="utf-8")
    for page_file in (
        "pages/17_First_Year_Growth_Plan.py",
        "pages/19_Sales_Coach.py",
        "pages/20_Market_Monitor.py",
        "pages/21_Quick_Subject_Briefing.py",
        "pages/22_Business_Networking_Desk.py",
        "pages/23_Relationship_Quarterback.py",
    ):
        assert page_file in app_source, f"Core workflow page is not registered: {page_file}"
