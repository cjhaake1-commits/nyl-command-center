from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def test_every_registered_navigation_target_exists():
    app_source = (ROOT / "app.py").read_text(encoding="utf-8")
    page_paths = re.findall(r'st\.Page\(["\']([^"\']+)["\']', app_source)
    assert page_paths, "No Streamlit pages were registered in app.py"
    missing = [page for page in page_paths if not (ROOT / page).is_file()]
    assert not missing, f"Registered navigation page(s) missing: {missing}"
