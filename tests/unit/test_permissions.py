import pytest

from astra_core.utils.permissions import ask_permission


@pytest.mark.unit
def test_permission_yes(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert ask_permission("test") is True


@pytest.mark.unit
def test_permission_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert ask_permission("test") is False
