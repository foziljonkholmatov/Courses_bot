from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.default import phone_keyboard

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Hi! Please send your phone number",
        reply_markup=phone_keyboard()
    )
