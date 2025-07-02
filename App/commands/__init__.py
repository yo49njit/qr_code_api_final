from abc import ABC, abstractmethod

class Command(ABC): 
    "Creating an abstract command class that my command classes can inherit"
    @abstractmethod
    def execute(self):
        pass

class CommandsHandler: 
    def __init__(self): 
        "Initializer"
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        "Register method"
        self.commands[command_name]= command

    def execute_command(self, command_name:str): 
        "Execute method"
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command as: {command_name} exists")