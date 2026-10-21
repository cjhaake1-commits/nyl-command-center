import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_registered_streamlit_pages_exist_and_parse():
    app_path = ROOT / "app.py"
    app_tree = ast.parse(app_path.read_text(encoding="utf-8"), filename=str(app_path))
    page_paths = [
        node.args[0].value
        for node in ast.walk(app_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "Page"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
    ]

    assert page_paths, "No Streamlit pages registered in app.py"
    for relative_path in page_paths:
        page_path = ROOT / relative_path
        assert page_path.is_file(), f"Registered page is missing: {relative_path}"
        source = page_path.read_text(encoding="utf-8")
        compile(source, str(page_path), "exec")
