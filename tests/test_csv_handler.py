import os
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.csv_handler import *
from calculator.operations import add
import pytest

def operation_lookup(name):
    return {
        'add': add
    }.get(name, None)

def test_save_and_load_csv(tmp_path):
    file = tmp_path / "test_history.csv"
    calc = Calculation(Decimal("2"), Decimal("3"), add)

    save_to_csv([calc], filename=str(file))
    assert file.exists()

    history = load_from_csv(filename=str(file), operation_lookup=operation_lookup)
    assert len(history) == 1
    assert history[0].perform() == Decimal("5")

def test_clear_csv(tmp_path):
    file = tmp_path / "to_delete.csv"
    file.write_text("temporary content")
    assert file.exists()

    clear_csv(str(file))
    assert not file.exists()

def test_clear_csv_file_not_exist(tmp_path, capsys):
    file = tmp_path / "nonexistent.csv"
    assert not file.exists()

    clear_csv(str(file))

    captured = capsys.readouterr()
    assert f"File {file} does not exist." in captured.out