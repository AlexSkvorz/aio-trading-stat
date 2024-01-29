from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from config.bot_config_example import BOT_CONFIG

bot = Bot(BOT_CONFIG['TOKEN'])
dispatcher = Dispatcher()


@dispatcher.message(Command("start"))
async def send_welcome_message(message):
    await message.answer(f"Привет, <b><i>{message.from_user.first_name}</i></b>", parse_mode="HTML")


@dispatcher.message()
async def send_insult(message):
    await message.answer("Ваня лох")

dispatcher.run_polling(bot)
