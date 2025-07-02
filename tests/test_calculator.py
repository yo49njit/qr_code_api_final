"""
Unit tests for the calculator module.
"""

from calculator import Calculator

def test_addition():
    """Test the add() function."""
    assert Calculator.add(2, 2) == 4
def test_subtraction():
    """Test the subtract() function."""
    assert Calculator.subtract(5, 2) == 3
def test_multiply():
    """Test the multiply() function."""
    assert Calculator.multiply(2, 4) == 8
def test_divide():
    """Test the divide() function."""
    assert Calculator.divide(20, 2) == 10
