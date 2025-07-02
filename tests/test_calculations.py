'''My Calculator Test'''
from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import *

from calculator.operations import *

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for testing."""
    Calculations.clear_history()

    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('4'), multiply))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    sample_calc = Calculation(Decimal('4'), Decimal('3'), add)

    Calculations.add_calculation(sample_calc)

    assert Calculations.get_last() == sample_calc, "Failed to add the calculation to the hitory"

def test_delete_calculation(setup_calculations):
    """Test deleting a calculation from the history."""
    sample_calc = Calculation(Decimal('4'), Decimal('3'), add)
    Calculations.add_calculation(sample_calc)

    Calculations.delete_calculation(sample_calc)

    with pytest.raises(ValueError):
        Calculations.delete_calculation(sample_calc)  # Should raise ValueError since it's already deleted

    assert sample_calc not in Calculations.get_history(), "Failed to delete the calculation from the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    log = Calculations.get_history()
    assert len(log) == 3, "history does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "hitory was not cleared"

def test_get_last(setup_calculations):
    """Test getting the latest calculation from the hitory."""
    latest = Calculations.get_last()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in hitory by type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"
    multiply_operations = Calculations.find_by_operation("multiply")
    assert len(multiply_operations) == 1, "Did not find the correct number of calculations with multiply operation"

