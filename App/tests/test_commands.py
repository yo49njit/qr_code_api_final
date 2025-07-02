import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from App.plugins.add import Add
from App.plugins.subtract import Subtract
from App.plugins.multiply import Multiply
from App.plugins.divide import Divide
from App.plugins.get_history import GetHistory
from App.plugins.clear_history import ClearHistory
from App.plugins.get_last import GetLast
from App.plugins.find_operation import FindOperation
from calculator import Calculations, Calculation
from decimal import Decimal 
from calculator.operations import *


import builtins

def test_add_command(monkeypatch, capsys):
    inputs = iter(['2', '3'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    add_command = Add()
    add_command.execute()
    
    captured = capsys.readouterr()
    assert "2.0 + 3.0 = 5.0" in captured.out

def test_subtract_command(monkeypatch, capsys):
    inputs = iter(['5', '3'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    subtract_command = Subtract()
    subtract_command.execute()
    
    captured = capsys.readouterr()
    assert "5.0 - 3.0 = 2.0" in captured.out

def test_multiply_command(monkeypatch, capsys):
    inputs = iter(['6', '6'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    multiply_command = Multiply()
    multiply_command.execute()
    
    captured = capsys.readouterr()
    assert "6.0 x 6.0 = 36.0" in captured.out

def test_divide_command(monkeypatch, capsys):
    inputs = iter(['10', '2'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    divide_command = Divide()
    divide_command.execute()
    
    captured = capsys.readouterr()
    assert "10.0 / 2.0 = 5.0" in captured.out

def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(['10', '0'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    divide_command = Divide()
    divide_command.execute()

    captured = capsys.readouterr()
    assert (
    "Cannot divide by zero." in captured.out
    or "Error" in captured.out
    or "Invalid input" in captured.out
)

def test_get_history_command(capsys):
    Calculations.clear_history()
    sample_calc = Calculation(Decimal('2'), Decimal('3'), add)
    Calculations.add_calculation(sample_calc)
    command = GetHistory()
    command.execute()
    captured = capsys.readouterr()
    assert "2" in captured.out and "3" in captured.out

def test_clear_history_command(capsys):
    command = ClearHistory()
    command.execute()
    captured = capsys.readouterr()
    assert "History cleared" in captured.out 

def test_get_last_command(capsys):
    Calculations.clear_history()
    sample_calc = Calculation(Decimal('2'), Decimal('3'), add)
    Calculations.add_calculation(sample_calc)
    sample_calc = Calculation(Decimal('4'), Decimal('5'), add)
    Calculations.add_calculation(sample_calc)
    command = GetLast()
    command.execute()
    captured = capsys.readouterr()
    assert "Last calculation: " in captured.out or "No calculations in history" in captured.out



