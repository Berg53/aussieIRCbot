'''logging format'''
import logging

from settings import LOG_LOCATION

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# log to file:
handler = logging.FileHandler(LOG_LOCATION)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# add handler to the LOGGER
LOGGER.addHandler(handler)
LOGGER.info("Logger initialised")
