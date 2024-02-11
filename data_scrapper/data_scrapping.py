import json
from dataclasses import dataclass

import pyppeteer
import time

from bs4 import BeautifulSoup

from config import scrapper_config
from data_scrapper.calculations import calculate_week_user_profits
from old_database import users_rights_table, weeks_stats_table
from utils import date_utils


@dataclass
class MonitorData:
    overall_balance: float
    overall_profit: float
    overall_profit_percent: float
    week_profit: float
    week_profit_percent: float


def dollars_to_number(dollars):
    return float(dollars.replace(' ', '').replace('$', '').replace(',', ''))


def percents_to_number(percents):
    return float(percents.replace('+', '').replace('%', ''))


async def scrap_data() -> MonitorData:
    # Launch the browser
    browser = await pyppeteer.launch(
        executablePath=scrapper_config.PYPPETEER_BROWSER_PATH
    )

    # Open a new browser page
    page = await browser.newPage()

    # Open our test file in the opened page
    await page.goto(scrapper_config.FX_MONITOR_LINK)

    # Wait for all dynamic data to load
    time.sleep(10)

    # Get page source code
    page_content = await page.content()

    # current_week_monday = get_current_week_monday()
    # # Get screenshot of the page
    # await page.screenshot({'path': f'{STORAGE_CONFIG["path_to_screens"]}/{current_week_monday}.png'})
    # TODO images to base64

    await browser.close()

    soup = BeautifulSoup(page_content, 'lxml')
    return MonitorData(
        overall_balance=dollars_to_number(soup.find('a', id='17542800balance').text),
        overall_profit=dollars_to_number(soup.find('span', id='17542800profit_total').text),
        week_profit=dollars_to_number(soup.find('span', id='17542800profit_w').text),
        overall_profit_percent=percents_to_number(soup.find('span', id='17542800profit_total_pr').text),
        week_profit_percent=percents_to_number(soup.find('span', id='17542800profit_w_pr').text),
    )


def get_current_week_profits(db_connection, actual_overall_balance):
    user_balances = users_rights_table.fetch_user_balances(db_connection)
    last_week_stat = weeks_stats_table.fetch_week_stat(db_connection, date_utils.get_last_week_monday())

    user_overall_profits, user_week_profits = calculate_week_user_profits(
        actual_overall_balance=actual_overall_balance,
        last_week_user_balances=user_balances,
        last_week_user_overall_profits=json.loads(last_week_stat[6]),
    )

    return user_overall_profits, user_week_profits


def update_user_balances(db_connection, user_week_profits):
    for user_tag, user_week_profit in user_week_profits.items():
        users_rights_table.update_balance(db_connection, user_tag, user_week_profit)


def save_week_stat(db_connection, monitor_data: MonitorData,
                   user_overall_profits, user_week_profits):
    weeks_stats_table.insert_week_profit(
        db_connection=db_connection,
        monday_date=date_utils.get_current_week_monday(),
        overall_balance=monitor_data.overall_balance,
        overall_profit=monitor_data.overall_profit,
        current_week_profit=monitor_data.week_profit,
        profit_percents=monitor_data.overall_profit_percent,
        current_week_profit_percents=monitor_data.week_profit_percent,
        user_overall_profits=json.dumps(user_overall_profits),
        user_week_profits=json.dumps(user_week_profits),
    )
