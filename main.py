from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from config.bot_config import BOT_CONFIG

bot = Bot(BOT_CONFIG['TOKEN'])
dispatcher = Dispatcher()

@dispatcher.message(Command("start"))
async def response(message):
    await message.answer(f"Привет, <b><i>{message.from_user.first_name}</i></b>", parse_mode="HTML")

@dispatcher.message()
async def offense(message):
    await message.answer("Ваня лох")

dispatcher.run_polling(bot)
