from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command

Token = "6400399221:AAGWQEG-QE0JxqZQztI018i-uXlgjoUAAXw"
bot = Bot(Token)
dispatcher = Dispatcher()

@dispatcher.message(Command("start"))
async def answer(message):
    await message.answer(f"Привет, <b><i>{message.from_user.first_name}</i></b>", parse_mode="HTML")

@dispatcher.message()
async def answer(message):
    await message.answer("Ваня лох")

dispatcher.run_polling(bot)