from App.commands import Command
from calculator import Calculator

class GetLast(Command):
    def execute(self):
        print(f'Last calculation: {Calculator.get_last_calculation()}')
