import os

from astra_core.utils.backup_manager import create_backup, restore_backup


def test_create_backup(tmp_path):
    file = tmp_path / "test.py"
    file.write_text("print('hello')", encoding="utf-8")

    backup = create_backup(str(file))

    assert os.path.exists(backup)


def test_restore_backup(tmp_path):
    file = tmp_path / "test.py"
    file.write_text("original", encoding="utf-8")

    create_backup(str(file))
    file.write_text("modified", encoding="utf-8")

    restore_backup(str(file))

    assert file.read_text(encoding="utf-8") == "original"


def test_restore_backup_missing(tmp_path):
    file = tmp_path / "test.py"
    file.write_text("data", encoding="utf-8")

    result = restore_backup(str(file))

    assert result is False