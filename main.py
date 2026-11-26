import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import get_token
from database.database import async_session, create_tables, shutdown_db
from handlers.routers import main_router
from middlewares.db import DbSessionMiddleware


async def main() -> None:
    bot = Bot(get_token(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await create_tables()

    dp.update.middleware(DbSessionMiddleware(async_session))

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    finally:
        await shutdown_db()
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
