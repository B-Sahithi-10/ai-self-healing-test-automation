"""Unit tests: report JSON shape."""

import json

import pytest

from astra_core.reports.report_generator import save_report


@pytest.mark.unit
def test_save_report_writes_json_with_timestamp(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    name = save_report({"mode": "test"}, filename="out.json")
    assert name == "out.json"
    data = json.loads((tmp_path / "out.json").read_text(encoding="utf-8"))
    assert data["mode"] == "test"
    assert "generated_at" in data
    assert len(data["generated_at"]) >= 10
