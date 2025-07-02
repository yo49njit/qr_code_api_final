from App.commands import Command
from calculator import Calculator

class ClearHistory(Command):
    def execute(self):
        Calculator.clear_calculations()
        print("History cleared")