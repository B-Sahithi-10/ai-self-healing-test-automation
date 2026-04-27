import json

import pytest

from astra_core.pipeline.full_pipeline import run_full_pipeline


@pytest.mark.unit
def test_full_pipeline_all_skipped(monkeypatch, tmp_path, run_from_project_root):
    # Always skip interactive steps
    monkeypatch.setattr("astra_core.pipeline.full_pipeline.ask_permission", lambda prompt: False)

    # Lint still runs before/after even when steps are skipped
    monkeypatch.setattr(
        "astra_core.pipeline.full_pipeline.python_lint",
        lambda folder_path: {"returncode": 0, "stdout": "All checks passed!", "stderr": ""},
    )

    report_file = run_full_pipeline(str(tmp_path))
    assert report_file == "astra_report.json"

    report = json.loads((run_from_project_root / report_file).read_text(encoding="utf-8"))
    assert report["folder"] == str(tmp_path)
    assert report["steps"]["ruff_autofix"].get("skipped") is True
    assert report["steps"]["isort"].get("skipped") is True
    assert report["steps"]["black"].get("skipped") is True
    assert report["steps"]["pytest"].get("skipped") is True


@pytest.mark.unit
def test_full_pipeline_all_executed(monkeypatch, tmp_path, run_from_project_root):
    # Always execute interactive steps
    monkeypatch.setattr("astra_core.pipeline.full_pipeline.ask_permission", lambda prompt: True)

    monkeypatch.setattr(
        "astra_core.pipeline.full_pipeline.python_lint",
        lambda folder_path: {"returncode": 0, "stdout": "All checks passed!", "stderr": ""},
    )
    monkeypatch.setattr(
        "astra_core.pipeline.full_pipeline.python_autofix",
        lambda folder_path: {"returncode": 0, "stdout": "autofix ok", "stderr": ""},
    )
    monkeypatch.setattr(
        "astra_core.pipeline.full_pipeline.python_sort_imports",
        lambda folder_path: {"returncode": 0, "stdout": "isort ok", "stderr": ""},
    )
    monkeypatch.setattr(
        "astra_core.pipeline.full_pipeline.python_format_black",
        lambda folder_path: {"returncode": 0, "stdout": "black ok", "stderr": ""},
    )
    monkeypatch.setattr(
        "astra_core.pipeline.full_pipeline.python_run_tests",
        lambda folder_path: {"returncode": 0, "stdout": "pytest ok", "stderr": ""},
    )

    report_file = run_full_pipeline(str(tmp_path))
    assert report_file == "astra_report.json"

    report = json.loads((run_from_project_root / report_file).read_text(encoding="utf-8"))
    steps = report["steps"]
    assert steps["ruff_autofix"]["stdout"] == "autofix ok"
    assert steps["isort"]["stdout"] == "isort ok"
    assert steps["black"]["stdout"] == "black ok"
    assert steps["pytest"]["stdout"] == "pytest ok"
