"""Integration: python_engine talks to real CLI tools (ruff, etc.)."""

import pytest

from astra_core.engines.python_engine import python_lint


@pytest.mark.integration
def test_python_lint_reports_unused_import(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bad = tmp_path / "lint_me.py"
    bad.write_text("import os\n\nx = 1\n", encoding="utf-8")

    result = python_lint(str(tmp_path))

    assert isinstance(result, dict)
    assert "returncode" in result
    assert result["returncode"] != 0
    assert "os" in result["stdout"] or "import" in result["stdout"].lower()
