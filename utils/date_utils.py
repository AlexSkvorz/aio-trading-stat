import datetime


def get_current_week_monday():
    today = datetime.date.today()

    return get_monday_by_week_date(today)


def get_last_week_monday():
    return get_current_week_monday() - datetime.timedelta(days=7)


def get_monday_by_week_date(week_date):
    days_since_monday = week_date.weekday()
    monday = week_date - datetime.timedelta(days=days_since_monday)

    return monday
