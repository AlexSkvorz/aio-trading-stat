import asyncio

from aiogram import Dispatcher, Bot
from config import bot_config
from telegram_bot.handlers import (start_command_handler, message_handler)
from config.database_config import POSTGRES_CONNECTION
from database.database_manager import DatabaseManager
from logs.logging import configure_logging


async def main():
    await configure_logging()
    db_manager = DatabaseManager(POSTGRES_CONNECTION)
    await db_manager.init_models()
    bot = Bot(bot_config.TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start_command_handler.router,
        message_handler.router,

    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
