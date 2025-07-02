
import os
import logging
from dotenv import load_dotenv

load_dotenv()

LOG_FILE_PATH = os.getenv("LOG_FILE_PATH")

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

"""Creating logger object naming it app_logger which will be reused everywhere to log"""

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

"""Prevent duplicate handlers so we dont have duplicates of the same log inside logs.txt"""
if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE_PATH)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
