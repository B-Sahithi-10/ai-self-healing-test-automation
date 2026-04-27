import json

import pytest

from astra_core.pipeline.ai_compile_fix_pipeline import run_ai_compile_fix


@pytest.mark.unit
def test_compile_pass_writes_empty_fixes(monkeypatch, tmp_path, run_from_project_root):
    ok = tmp_path / "ok.py"
    ok.write_text("print('ok')\n", encoding="utf-8")

    monkeypatch.setattr(
        "astra_core.pipeline.ai_compile_fix_pipeline.scan_project_files",
        lambda folder_path, extensions=(".py",): [str(ok)],
    )
    monkeypatch.setattr(
        "astra_core.pipeline.ai_compile_fix_pipeline.python_compile_check",
        lambda file_path: {"returncode": 0, "stderr": ""},
    )

    report_file = run_ai_compile_fix(str(tmp_path))
    assert report_file == "astra_ai_compile_report.json"

    report = json.loads((run_from_project_root / report_file).read_text(encoding="utf-8"))
    assert report["files_checked"] == 1
    assert report["fixes"] == []


@pytest.mark.unit
def test_ai_returns_empty_rolls_back(monkeypatch, tmp_path, run_from_project_root):
    bad = tmp_path / "bad.py"
    bad.write_text("print(\n", encoding="utf-8")  # syntax error

    monkeypatch.setattr(
        "astra_core.pipeline.ai_compile_fix_pipeline.scan_project_files",
        lambda folder_path, extensions=(".py",): [str(bad)],
    )

    # First compile fails, second compile result won't be reached (AI empty)
    monkeypatch.setattr(
        "astra_core.pipeline.ai_compile_fix_pipeline.python_compile_check",
        lambda file_path: {"returncode": 1, "stderr": "SyntaxError: invalid syntax"},
    )

    monkeypatch.setattr(
        "astra_core.pipeline.ai_compile_fix_pipeline.ask_permission",
        lambda prompt: True,
    )

    calls = {"backup": 0, "restore": 0}

    def _backup(_path):
        calls["backup"] += 1
        return str(bad) + ".bak"

    def _restore(_path):
        calls["restore"] += 1
        return True

    monkeypatch.setattr("astra_core.pipeline.ai_compile_fix_pipeline.create_backup", _backup)
    monkeypatch.setattr("astra_core.pipeline.ai_compile_fix_pipeline.restore_backup", _restore)

    # AI returns empty -> ai_fix_file returns None
    monkeypatch.setattr(
        "astra_core.pipeline.ai_compile_fix_pipeline.call_ollama",
        lambda prompt, model="qwen2.5-coder:3b": "",
    )

    report_file = run_ai_compile_fix(str(tmp_path))
    assert report_file == "astra_ai_compile_report.json"

    report = json.loads((run_from_project_root / report_file).read_text(encoding="utf-8"))
    assert report["files_checked"] == 1
    assert report["fixes"][0]["status"] == "failed"
    assert report["fixes"][0]["reason"] == "Empty AI output"
    assert calls["backup"] == 1
    assert calls["restore"] == 1
