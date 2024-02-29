# log_dir - Gets the absolute path to the "logs" directory in the project root
# log_file - Gets the absolute path to file, containing "yourname_file.log" in the "logs" directory
import os

log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
log_file = os.path.join(log_dir, 'your_file.log')
