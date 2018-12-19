import logging

from settings import LOG_LOCATION

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Format logs:
file_handler = logging.FileHandler(LOG_LOCATION)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add handler and formatter to logger:
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
