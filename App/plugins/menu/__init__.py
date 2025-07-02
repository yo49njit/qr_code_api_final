from App.commands import Command
"dynamic menu that updates based on plugins folders"

class Menu(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        print("\nAvailable Commands:")
        for key in self.command_handler.commands:
            print(f" - {key}")
