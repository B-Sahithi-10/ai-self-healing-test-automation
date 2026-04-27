from unittest.mock import Mock, patch

import pytest

from astra_core.ai.ollama_engine import call_ollama


@pytest.mark.unit
@patch("astra_core.ai.ollama_engine.subprocess.run")
def test_ollama_call_success(mock_run):
    mock_run.return_value = Mock(returncode=0, stdout="fixed code\n")

    result = call_ollama("bad code")

    assert "fixed code" == result


@pytest.mark.unit
@patch("astra_core.ai.ollama_engine.subprocess.run")
def test_ollama_call_nonzero_returncode_returns_empty(mock_run):
    mock_run.return_value = Mock(returncode=1, stdout="should be ignored", stderr="boom")

    result = call_ollama("bad code")

    assert result == ""


@pytest.mark.unit
@patch("astra_core.ai.ollama_engine.subprocess.run", side_effect=Exception("fail"))
def test_ollama_exception_returns_empty(_mock_run):
    result = call_ollama("code")

    assert result == ""
