import logging
from config.logging_config import log_file


def configure_logging():
    logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')
