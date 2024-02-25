# log_dir - Gets the absolute path to the ‘logs’ directory in the project root
# log_file - Gets the absolute path to file, containing ‘yourname_file.log’ in the ‘logs’ directory
# def - Configures the logging module to log messages to ‘yourname_file.log’, with a specific format.

import os
import logging

log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
log_file = os.path.join(log_dir, 'yourname_file.log')


def configure_logging():
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
