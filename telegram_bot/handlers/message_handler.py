from aiogram import Router

router = Router()


@router.message()
async def send_insult(message):
    await message.answer("Ваня лох")
