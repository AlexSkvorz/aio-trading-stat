import asyncio
import pathlib
import logging
import sys

from celery import Celery
from celery.schedules import crontab

from data_scrapper.monitor_data import MonitorData

root_path = pathlib.Path(__file__).parent.parent
sys.path.append(str(root_path))

from old_database.create_connection import create_db_connection
from config import scrapper_config
from data_scrapper import data_scrapping


RETRYING_TIME_SEC = 60
MAX_RETRIES = 600

CELERY_BEAT_SCHEDULE = {
    'weekly-scrapping': {
        'task': 'scrap_data_task.scrap_data_task',
        'schedule': crontab(
            day_of_week=scrapper_config.SCRAP_WEEK_DAY,
            hour=scrapper_config.SCRAP_HOUR,
            minute='0'
        ),
    },
}

app = Celery(
    main='data_scrapper',
    broker=scrapper_config.MESSAGE_BROKER_URL,
)
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE


@app.task(bind=True)
def scrap_data_task(self):
    db_connection = create_db_connection()
    logging.info("Start scraping data...")
    monitor_data: MonitorData = asyncio.run(data_scrapping.scrap_data())
    if monitor_data:
        logging.info("Data was scrapped successfully!")
        logging.info("Saving scrapped data to database...")

        user_overall_profits, user_week_profits = data_scrapping.get_current_week_profits(
            db_connection, monitor_data.overall_balance
        )
        data_scrapping.save_week_stat(db_connection, monitor_data, user_overall_profits, user_week_profits)
        data_scrapping.update_user_balances(db_connection, user_week_profits)

        logging.info("Data was saved successfully!")
    else:
        logging.error(f"Error while scraping data! "
                      f"Will try again after {RETRYING_TIME_SEC} sec")
        self.retry(countdown=RETRYING_TIME_SEC, max_retries=MAX_RETRIES)
