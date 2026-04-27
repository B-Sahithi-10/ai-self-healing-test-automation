"""End-to-end: invoke main.py as a separate process (black-box CLI)."""

import json
import subprocess
import sys

import pytest


@pytest.mark.e2e
def test_cli_scanall_demo_project(project_root):
    """Invokes CLI with cwd=project root (where demo_project and main.py live)."""
    proc = subprocess.run(
        [sys.executable, "main.py", "scanall", "demo_project"],
        cwd=project_root,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert proc.returncode == 0, proc.stderr
    assert "SCANALL completed." in proc.stdout
    report_path = project_root / "astra_scanall_report.json"
    assert report_path.is_file()
    data = json.loads(report_path.read_text(encoding="utf-8"))
    assert data.get("mode") == "scanall"
    assert data.get("folder") == "demo_project"
    assert data.get("files_scanned", 0) >= 1
