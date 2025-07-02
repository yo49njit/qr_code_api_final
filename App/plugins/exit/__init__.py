from App.commands import Command
import sys

class Exit(Command):
    def execute(self):
        sys.exit("Program exitted")