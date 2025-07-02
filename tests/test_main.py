import pytest
from main import calculate_and_print 

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("4", "2", 'add', "The result of 4 add 2 is equal to 6"),
    ("2", "2", 'subtract', "The result of 2 subtract 2 is equal to 0"),
    ("5", "6", 'multiply', "The result of 5 multiply 6 is equal to 30"),
    ("40", "4", 'divide', "The result of 40 divide 4 is equal to 10"),
    ("1", "0", 'divide', "An unexpected error has occurred: Cannot divide by zero."),  
    ("2", "1", 'unknown', "Unknown operation: unknown"),  
    ("a", "3", 'multiply', "Invalid number input: a or 3 is not a valid number."), 
    ("9", "b", 'add', "Invalid number input: 9 or b is not a valid number.")  
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string