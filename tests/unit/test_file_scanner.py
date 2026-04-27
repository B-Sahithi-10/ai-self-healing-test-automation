"""Unit tests: file discovery rules (no subprocess)."""

import os

import pytest

from astra_core.utils.file_scanner import scan_project_files


@pytest.mark.unit
def test_scan_collects_py_files(tmp_path):
    (tmp_path / "a.py").write_text("x=1\n", encoding="utf-8")
    (tmp_path / "b.py").write_text("y=2\n", encoding="utf-8")
    files = scan_project_files(str(tmp_path))
    assert len(files) == 2
    assert all(f.endswith(".py") for f in files)


@pytest.mark.unit
def test_scan_skips_bak_and_json(tmp_path):
    (tmp_path / "ok.py").write_text("pass\n", encoding="utf-8")
    (tmp_path / "skip.bak").write_text("", encoding="utf-8")
    (tmp_path / "data.json").write_text("{}", encoding="utf-8")
    files = scan_project_files(str(tmp_path))
    assert len(files) == 1
    assert files[0].endswith("ok.py")


@pytest.mark.unit
def test_scan_accepts_single_py_file_path(tmp_path):
    f = tmp_path / "only.py"
    f.write_text("x = 1\n", encoding="utf-8")
    files = scan_project_files(str(f))
    assert len(files) == 1
    assert os.path.samefile(files[0], f)


@pytest.mark.unit
def test_scan_skips_ignored_directories(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "m.py").write_text("pass\n", encoding="utf-8")
    vdir = tmp_path / ".venv"
    vdir.mkdir()
    (vdir / "bad.py").write_text("syntax error here\n", encoding="utf-8")
    files = scan_project_files(str(tmp_path))
    paths = [f.replace("\\", "/") for f in files]
    assert any(p.endswith("pkg/m.py") for p in paths)
    assert not any(".venv" in p for p in paths)
