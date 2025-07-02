# Project install instructions

1.clone
2.pip install -r requirments.txt

##Testing
1. pytest
2.pytest --pylint
3.pytest --pylint --cov   

# video
can be found at (https://drive.google.com/drive/folders/1-CdxOUPztQ8vS6rCfJr58xTFbTC_UsCB)
# Logging
I used logging by creating a logger.py inside data folder and configuring it so that it saves all logs to logs.txt inside data folder
i wanted to avoid repudation so i created the logger.py as kind of a module that i can call on in every file where i needed logging without having
to reconfigure it in every file needed . now whenever i need to log something i import this line

///////////////////////////////
"from data.logger import logger"
////////////////////////////////

and use it by writing


/////////////////////////////
"logger.info("Message")"
//////////////////////////////

i focused on logging the instances were the app was used so once in App/main.py then used logger object in __init__.py inside calculator folder so it logs the operations being used, and when history has any action done to it. i wanted logs to be permenant and follow every action so i didnt create a way to delete it. I wanted to focus my logging on the use of the App so i didnt log the errors created by tests purposfully

# environmental variables

instead of hardcoding the addresses where history.csv is and log.txt i created a .env file that stored the addresses

CSV_HISTORY_PATH=data/history.csv
LOG_FILE_PATH=data/log.txt

and when i need them import load_dotenv() from dotenv and load_dotenv() in the beginning of everyfile where theyre addresses is needed then create a variable that stores the address like for example

///////////////////////////////////////////
CSV_FILE = os.getenv("CSV_HISTORY_PATH", "default_history.csv") #in csv_handler.py
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH") #in logger.py
///////////////////////////////////////////////

# Look before you Leap and Easier to ask for forgivness than permission 

I used Easier to ask for forgivness than permission all throughout my code but some examples in my code where it was used is in main.py

/////////////////////////////////////////////
def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name)
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: 
        print(f"An unexpected error has occurred: {e}")
//////////////////////////////////////////////

and in commands/__init__

//////////////////////////////////////////
    def execute_command(self, command_name:str): 
        "Execute method"
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command as: {command_name} exists")
/////////////////////////////////////////////


I used look before you leap all throughout my code but some examples in my code where it was used is in my operations.py

//////////////////////////////////////////////
@staticmethod
def divide(a: Decimal, b: Decimal) -> Decimal:
    """Returns the division of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
//////////////////////////////////////////////

and in csv.handler

///////////////////////////////////////////////
def clear_csv(filename: str = CSV_FILE):
    """Clear the CSV file."""
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"File {filename} does not exist.")
///////////////////////////////////////////////


# Design patterns for Scalable Architecture

Facade patterns:
offering a simple inteface and hiding complex modules, i did that by having all functions involving a csv be handled by csv_handler.py then importing it in calculations.py and calling the needed meothods with approriate methods. example in calculations.py

//////////////////////////////////////////////////////////
@classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history list."""
        cls.history.append(calculation)
        save_to_csv(cls.history)
//////////////////////////////////////////////////////

then calculations.py is imported to the __init__ inside calculator which conatians all necessary functionalities. __init__ becomes the contact point between the logic of the calculator and the command line interface

Command pattern:
insdie App there is a plugins folder ad every single command has its own directory with it's own __init__ file. the __init__  of app has the functionality to transform every folder into a command that will be used in the command line interface

add plugin
/////////////////////////////////////////////////////////
from App.commands import Command
from calculator import Calculator

class Add(Command):
    def execute(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = Calculator.add(a, b)
        print(f"{a} + {b} = {result}")

//////////////////////////////////////////////////////////

Factory method:
an example where i used factory method in my code is in main.py calculate_print method

///////////////////////////////////////////////////////////
operation_mappings = {
    'add': Calculator.add,
    'subtract': Calculator.subtract,
    'multiply': Calculator.multiply,
    'divide': Calculator.divide
}
/////////////////////////////////////////////////////////////

this demonstrates factory method because it provides a method to create objects without specifying the exact class of the object.

another example is the calculation class in calculation.py

////////////////////////////////////////////////////////////
class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
//////////////////////////////////////////////////////////////

singleton pattern:
to demonstrate the use of singleton patter i need to show a class that only has one instance with a gloable point of entry. this is demonstartaed in logger in logger.py

/////////////////////////////////////////
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

"""Prevent duplicate handlers so we dont have duplicates of the same log inside logs.txt"""
if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE_PATH)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
//////////////////////////////////////////

one logger that is used all throughout the code with single point of entry being from logger.py and no matter how many times its called there will only be one logger pushing all information to a single file

Strategy pattern:
having a family of algorithms (strategies), and encapsulating each one so that they can be interchangable. this can be seen in calcualtion.py

////////////////////////////////////////////////////////
class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
//////////////////////////////////////////////////////////////

by using operation as a parameter i used startegy pattern because i can plug in any desired operation, and if i created new operations they could be passed too as long as they only involve 2 variables

