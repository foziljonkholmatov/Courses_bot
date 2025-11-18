import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.contact import router as contact_router
from handlers.courses import router as course_router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(contact_router)
    dp.include_router(course_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
