import logging
from config.logging_config import LOGFILE, LOGLEVEL, LOGFORMAT


async def configure_logging():
    logging.basicConfig(filename=LOGFILE, level=LOGLEVEL, format=LOGFORMAT)
