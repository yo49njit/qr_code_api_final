import pytest
from decimal import Decimal
from calculator.calculation import *
from calculator.operations import *

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal("5"), Decimal("3"), add, Decimal("8")),
    (Decimal("10"), Decimal("2"), subtract, Decimal("8")),
    (Decimal("4"), Decimal("2"), multiply, Decimal("8")),
    (Decimal("16"), Decimal("2"), divide, Decimal("8"))
])
def test_operation(a, b, operation, expected):
    '''Function for testing all operations'''
    calculation = Calculation(a, b, operation)
    assert calculation.perform() == expected, "operation failed"

def test_divide_by_zero():
    '''Function for testing divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('1'), Decimal('0'), divide)
        calculation.perform()