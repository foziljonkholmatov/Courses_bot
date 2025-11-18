from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import COURSES


def phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Send your phone', request_contact=True)]
        ],
        resize_keyboard=True
    )


def courses_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=c)] for c in COURSES
        ],
        resize_keyboard=True
    )