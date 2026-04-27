from pathlib import Path

import pytest

# Project root: .../astra copy/astra copy/
PROJECT_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def project_root():
    return PROJECT_ROOT


@pytest.fixture
def run_from_project_root(monkeypatch):
    """Many pipelines write reports relative to CWD."""
    monkeypatch.chdir(PROJECT_ROOT)
    return PROJECT_ROOT


@pytest.fixture
def tmp_py_package(tmp_path):
    """Minimal tree: pkg/clean.py and pkg/bad_syntax.py"""
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "clean.py").write_text("x = 1\n", encoding="utf-8")
    (pkg / "bad_syntax.py").write_text("def broken(\n", encoding="utf-8")
    return tmp_path
