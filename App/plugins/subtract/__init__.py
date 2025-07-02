from App.commands import Command
from calculator import Calculator

class Subtract(Command):
    def execute(self):
        try:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            output= Calculator.subtract(a,b)
            print(f"{a} - {b} = {output}")
        except ValueError:
            print("Invalid input")