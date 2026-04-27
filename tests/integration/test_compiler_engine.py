"""Integration: py_compile via compiler_engine (real Python subprocess)."""

import pytest

from astra_core.engines.compiler_engine import python_compile_check


@pytest.mark.integration
def test_compile_check_passes_on_valid_file(tmp_path):
    f = tmp_path / "ok.py"
    f.write_text("def f():\n    return 1\n", encoding="utf-8")
    r = python_compile_check(str(f))
    assert r["returncode"] == 0
    assert r["stderr"] == ""


@pytest.mark.integration
def test_compile_check_fails_on_syntax_error(tmp_path):
    f = tmp_path / "bad.py"
    f.write_text("def x(\n", encoding="utf-8")
    r = python_compile_check(str(f))
    assert r["returncode"] != 0
    assert "SyntaxError" in r["stderr"] or "error" in r["stderr"].lower()
