from aiogram import Router
from aiogram.types import Message

from config import USERS_FILE
from utils.csv_files import append_csv
from keyboards.default import courses_keyboard

router = Router()


@router.message(lambda msg: msg.contact is not None)
async def contact_handler(message: Message):
    user = message.from_user
    phone = message.contact.phone_number

    append_csv(USERS_FILE, {
        "user_id": user.id,
        "phone": phone
    })

    await message.answer("Thank you! Choice courses", reply_markup=courses_keyboard())
