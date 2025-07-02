from App.commands import Command
from calculator import Calculator

class Add(Command):
    def execute(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = Calculator.add(a, b)
        print(f"{a} + {b} = {result}")
