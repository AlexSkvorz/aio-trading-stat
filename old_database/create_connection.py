import sqlite3

from config import database_config
from old_database import deposit_info_table
from old_database import users_rights_table
from old_database import weeks_stats_table


def create_db_connection():
    db_connection = sqlite3.connect(database_config.DATABASE_FILE_NAME, check_same_thread=False)
    deposit_info_table.create_table(db_connection)
    users_rights_table.create_table(db_connection)
    weeks_stats_table.create_table(db_connection)
    return db_connection
