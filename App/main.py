import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from App import App
from data.logger import logger
import logging
   

if __name__ == "__main__":
    logger.info("User started app")
    app= App().start()