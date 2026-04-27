import json

import pytest

from astra_core.pipeline.ai_full_pipeline import run_full_pipeline_with_ai


@pytest.mark.unit
def test_full_pipeline_all_steps_mocked(monkeypatch, tmp_path, run_from_project_root):
    # Make every prompt auto-skip so the pipeline is non-interactive
    monkeypatch.setattr("astra_core.pipeline.ai_full_pipeline.ask_permission", lambda prompt: False)

    # Lint calls still happen (before/after each stage) even if stages are skipped
    monkeypatch.setattr(
        "astra_core.pipeline.ai_full_pipeline.python_lint",
        lambda folder_path: {"returncode": 0, "stdout": "All checks passed!", "stderr": ""},
    )

    # These won't be used because ask_permission returns False, but stub anyway for safety
    monkeypatch.setattr(
        "astra_core.pipeline.ai_full_pipeline.python_autofix",
        lambda folder_path: {"returncode": 0, "stdout": "", "stderr": ""},
    )
    monkeypatch.setattr(
        "astra_core.pipeline.ai_full_pipeline.python_sort_imports",
        lambda folder_path: {"returncode": 0, "stdout": "", "stderr": ""},
    )
    monkeypatch.setattr(
        "astra_core.pipeline.ai_full_pipeline.python_format_black",
        lambda folder_path: {"returncode": 0, "stdout": "", "stderr": ""},
    )
    monkeypatch.setattr("astra_core.pipeline.ai_full_pipeline.run_ai_compile_fix", lambda folder_path: "x.json")
    monkeypatch.setattr("astra_core.pipeline.ai_full_pipeline.run_runtime_fix", lambda folder_path: "y.json")
    monkeypatch.setattr(
        "astra_core.pipeline.ai_full_pipeline.python_run_tests",
        lambda folder_path: {"returncode": 0, "stdout": "", "stderr": ""},
    )

    report_file = run_full_pipeline_with_ai(str(tmp_path))
    assert report_file == "astra_fullscan_ai_report.json"

    report = json.loads((run_from_project_root / report_file).read_text(encoding="utf-8"))
    assert report["folder"] == str(tmp_path)

    steps = report["steps"]
    assert "lint_before" in steps
    assert steps["ruff_autofix"].get("skipped") is True
    assert steps["isort"].get("skipped") is True
    assert steps["black"].get("skipped") is True
    assert steps["compile_ai_report"].get("skipped") is True
    assert steps["runtime_fix"].get("skipped") is True
    assert steps["pytest"].get("skipped") is True
