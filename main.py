import asyncio

from aiogram import Dispatcher, Bot
from config import bot_config
from telegram_bot.handlers import (start_command_handler, message_handler)


async def main():
    bot = Bot(bot_config.TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start_command_handler.router,
        message_handler.router,

    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
