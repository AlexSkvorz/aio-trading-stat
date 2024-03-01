import logging
from config.logging_config import LOGFILE


def configure_logging():
    logging.basicConfig(filename=LOGFILE, level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')
