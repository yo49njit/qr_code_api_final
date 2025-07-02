from App.commands import Command
from calculator import Calculator

class FindOperation(Command):
    def execute(self):
        user= input("What opperation do you want to look up:")

        if user.lower() in ["add","subtract","multiply","divide"]:
            output= Calculator.find_calculations_by_operation(user.lower())
            for calc in output:
                print(calc)
        else:
            raise ValueError("Invalid Operation")

