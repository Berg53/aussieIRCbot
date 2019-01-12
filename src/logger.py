'''script for formatting logs'''
import logging

from settings import LOG_LOCATION

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# log to file:
HANDLER = logging.FileHandler(LOG_LOCATION)

FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
HANDLER.setFormatter(FORMATTER)

# add HANDLER to the LOGGER
LOGGER.addHandler(HANDLER)
LOGGER.info("Logger initialised")
