from App.commands import Command
from calculator import Calculator

class GetHistory(Command):
    def execute(self):
        for calc in Calculator.get_calculations():
            print(calc)