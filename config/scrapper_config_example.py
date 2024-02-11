# Message broker server URL. You can use any broker,
# such as RabbitMQ or Redis.
# This is an example of RabbitMQ default URL.
MESSAGE_BROKER_URL = 'amqp://guest:guest@localhost//'

# Path to browser executable file path using by pyppeteer.
# Pyppeteer can download browser by itself, but
# sometimes it may not work.
# If you want to use browser, downloaded by Pyppeteer,
# please specify this parameter as None.
PYPPETEER_BROWSER_PATH = '/usr/bin/chromium'

FX_MONITOR_LINK = 'https://fxmonitor.online/...?view=pro&mode=2'
SCRAP_WEEK_DAY = '6'  # Saturday by default
SCRAP_HOUR = '0'  # !Time in UTC!
