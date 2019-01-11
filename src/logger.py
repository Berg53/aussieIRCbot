import logging

from settings import LOG_LOCATION

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# log to file:
handler = logging.FileHandler(LOG_LOCATION)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# add handler to the logger
logger.addHandler(handler)
logger.info("Logger initialised")
