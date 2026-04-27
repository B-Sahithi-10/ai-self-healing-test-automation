import json

import pytest

from astra_core.pipeline.ai_fix_pipeline import run_ai_fix_only


@pytest.mark.unit
def test_ai_fix_empty(monkeypatch, tmp_path, run_from_project_root):
    bad = tmp_path / "bad.py"
    bad.write_text("print(\n", encoding="utf-8")

    # Pretend Ruff found a syntax issue in bad.py using the arrow format
    fake_ruff_out = "invalid-syntax: Expected `)`, found newline\n --> bad.py:1:7\n"
    monkeypatch.setattr(
        "astra_core.pipeline.ai_fix_pipeline.python_lint",
        lambda folder_path: {"returncode": 1, "stdout": fake_ruff_out, "stderr": ""},
    )

    # Ensure the pipeline detects the file and attempts to fix it
    monkeypatch.setattr("astra_core.pipeline.ai_fix_pipeline.ask_permission", lambda prompt: True)

    # AI returns empty output
    monkeypatch.setattr("astra_core.pipeline.ai_fix_pipeline.call_ollama", lambda prompt, model="qwen2.5-coder:3b": "")

    report_file = run_ai_fix_only(str(tmp_path))
    assert report_file == "astra_ai_report.json"

    report = json.loads((run_from_project_root / report_file).read_text(encoding="utf-8"))
    assert report["mode"] == "aifix"
    assert report["folder"] == str(tmp_path)
    assert report["ruff_lint"]["returncode"] == 1
    assert len(report["ai_fixes"]) == 1
    assert report["ai_fixes"][0]["file"].endswith("bad.py")
    assert report["ai_fixes"][0]["result"]["status"] == "failed"
    assert report["ai_fixes"][0]["result"]["reason"] == "Empty AI response"
