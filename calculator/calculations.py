from decimal import Decimal
from typing import Callable, List
import os
from calculator.calculation import *
from calculator.csv_handler import *


class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history list."""
        cls.history.append(calculation)
        save_to_csv(cls.history)

    @classmethod 
    def delete_calculation(cls, calculation: Calculation):
        """Remove a calculation from the history list."""
        if calculation in cls.history:
            cls.history.remove(calculation)
            save_to_csv(cls.history)
        else:
            raise ValueError("Calculation not found in history.")

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()
        clear_csv()

    @classmethod
    def get_last(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return "No calculations in history"

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    @classmethod
    def print_from_history(cls):
            return f"{self.a} {self.operation.__name__} {self.b} = {self.perform()}"


    
            

    
 