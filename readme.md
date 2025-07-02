# Project install instructions

1.clone
2.pip install -r requirments.txt

##Testing
1. pytest
2.pytest --pylint
3.pytest --pylint --cov   

# Logging
I used logging by creating a logger.py inside data folder and configuring it so that it saves all logs to logs.txt inside data folder
i wanted to avoid repudation so i created the logger.py as kind of a module that i can call on in every file where i needed logging without having
to reconfigure it in every file needed . now whenever i need to log something i import this line

"from data.logger import logger"

and use it by writing

"logger.info("Message")"

i focused on logging the instances were the app was used so once in App/main.py then used logger object in __init__.py inside calculator folder so it logs the operations being used, and when history has any action done to it. i wanted logs to be permenant and follow every action so i didnt create a way to delete it. I wanted to focus my logging on the use of the App so i didnt log the errors created by tests purposfully

# environmental variables

instead of hardcoding the addresses where history.csv is and log.txt i created a .env file that stored the addresses

CSV_HISTORY_PATH=data/history.csv
LOG_FILE_PATH=data/log.txt

and when i need them import load_dotenv() from dotenv and load_dotenv() in the beginning of everyfile where theyre addresses is needed then create a variable that stores the address like for example

CSV_FILE = os.getenv("CSV_HISTORY_PATH", "default_history.csv") in csv_handler.py
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH") in logger.py

# Look before you Leap and Easier to ask for forgivness than permission 




