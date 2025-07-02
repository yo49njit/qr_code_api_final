import pkgutil
import importlib
from App.commands import CommandsHandler
from App.commands import Command

class App:
    def __init__(self):
        self.command_handler = CommandsHandler()

    def load_plugins(self):
        plugins_package = 'App.plugins'
        package = importlib.import_module(plugins_package)

        print("Searching plugins in:", package.__path__)  # Debug print

        for _, plugin_name, is_pkg in pkgutil.iter_modules(package.__path__):
            if is_pkg:  
                plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")

                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                        command_key = item.__name__.lower()

                        if command_key == "menu":
                            instance = item(self.command_handler)
                        else:
                            instance = item()
                        self.command_handler.register_command(command_key, instance)



    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())


