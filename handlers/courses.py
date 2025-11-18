from aiogram import Router
from aiogram.types import Message

from config import COURSES
from utils.courses_settings import is_member, save_course

router = Router()


@router.message()
async def course_handler(message: Message):
    course = message.text
    user_id = message.from_user.id

    if course not in COURSES:
        await message.answer("Course not found!")
        return

    if is_member(user_id, course):
        await message.answer(f"'{course}' Already choice.")
        return

    save_course(user_id, course)
    await message.answer(f"'{course}' Successfully")
