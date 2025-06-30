from decimal import Decimal 

@staticmethod
def add(a:Decimal, b:Decimal) -> Decimal:
    """Returns the sum of a and b."""
    return a + b

@staticmethod
def subtract(a:Decimal, b:Decimal) -> Decimal:
    """Returns the difference of a and b."""
    return a - b

@staticmethod
def multiply(a:Decimal, b:Decimal) -> Decimal:
    """Returns the multiplication of a and b."""
    return a * b

@staticmethod
def divide(a:Decimal, b:Decimal) -> Decimal:
    """Returns the division of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b