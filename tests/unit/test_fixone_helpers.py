"""Unit tests: fixone_pipeline string helpers."""

import pytest

from astra_core.pipeline.fixone_pipeline import clean_ai_output, is_valid_python_code


@pytest.mark.unit
def test_clean_ai_output_strips_markdown_fence():
    raw = "```python\nx = 1\n```"
    assert clean_ai_output(raw).strip() == "x = 1"


@pytest.mark.unit
def test_is_valid_python_code_rejects_empty():
    assert is_valid_python_code("") is False


@pytest.mark.unit
def test_is_valid_python_code_accepts_simple_module():
    code = "import os\ndef f():\n    return 1\n"
    assert is_valid_python_code(code) is True
