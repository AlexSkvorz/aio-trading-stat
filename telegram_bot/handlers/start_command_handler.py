from aiogram import Dispatcher, Router
from aiogram.filters.command import Command

router = Router()


@router.message(Command("start"))
async def send_welcome_message(message):
    await message.answer(f"Привет, <b><i>{message.from_user.first_name}</i></b>", parse_mode="HTML")
