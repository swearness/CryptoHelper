from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from services.menu import show_main_menu
from services.user import register_user

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, session: AsyncSession) -> None:
    await register_user(
        session=session,
        user_id=message.from_user.id,
        username=message.from_user.username,
    )

    await show_main_menu(message, str(message.from_user.first_name))
