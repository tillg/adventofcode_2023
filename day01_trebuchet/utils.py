import json
import os
import pathlib
import re as re

from datetime import datetime, timedelta
from typing import Dict,  Optional
from sys import exit
import logging

INTERNAL_DATE_FORMAT = "%Y-%m-%d"


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


internalDateFormat = "%Y-%m-%d %H:%M:%S"


def get_logger(name, log_level=logging.WARN):
    # Get a logger with the given name
    logger = logging.getLogger(name)
    # Disable propagation to the root logger. Makes sense in Jupyter only...
    logger.propagate = False
    logger.setLevel(log_level)

    # Check if the logger has handlers already
    if not logger.handlers:
        # Create a handler
        handler = logging.StreamHandler()

        # Set a format that includes the logger's name
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def stripBlanks(str):
    return str.strip(" \t")
