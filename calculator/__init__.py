"""
Calculator module containing basic arithmetic operations.
"""
from calculator.calculations import *
from calculator.operations import *
from calculator.calculation import * 
from decimal import Decimal  
from typing import Callable 
from data.logger import logger

class Calculator:
    @staticmethod
    def perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation(a, b, operation)
        Calculations.add_calculation(calculation)
        logger.info(f"The {operation} operation was performed on {a} and {b}")
        return calculation.perform()
    

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, divide)
    
    @staticmethod
    def get_calculations() -> list:
        """Return a list of all calculations."""
        logger.info("User fetched history")
        return Calculations.get_history()
    
    @staticmethod
    def clear_calculations():
        """Clear all calculations."""
        logger.info("User cleared history")
        Calculations.clear_history()

    @staticmethod
    def get_last_calculation() -> Calculation:
        """Return the last calculation."""
        logger.info("User fetched last calculation")
        return Calculations.get_last()
    
    @staticmethod
    def find_calculations_by_operation(operation_name: str) -> list:
        """Find calculations by operation name."""
        logger.info(f"User looked for all {operation_name} calculations")
        return Calculations.find_by_operation(operation_name)

    