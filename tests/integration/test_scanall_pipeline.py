"""Integration: scan_all + real tools (ruff, py_compile, python run) on temp tree."""

import json

import pytest

from astra_core.pipeline.scanall_pipeline import scan_all


@pytest.mark.integration
def test_scan_all_detects_syntax_error(tmp_py_package, monkeypatch):
    monkeypatch.chdir(tmp_py_package)
    report_file, report = scan_all(str(tmp_py_package))
    assert report_file == "astra_scanall_report.json"
    assert report["mode"] == "scanall"
    assert report["files_scanned"] >= 1
    assert len(report["files_with_errors"]) >= 1
    types = {e["type"] for item in report["files_with_errors"] for e in item["errors"]}
    assert "syntax" in types
    written = json.loads((tmp_py_package / report_file).read_text(encoding="utf-8"))
    assert written["files_scanned"] == report["files_scanned"]
