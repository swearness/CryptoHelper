from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.main_menu import keyboard
from services.user_service import register_user

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, session: AsyncSession) -> None:
    await register_user(
        session=session,
        user_id=message.from_user.id,
        username=message.from_user.username,
    )

    await message.answer(
        f"""
        👋 Hi, {html.bold(message.from_user.first_name)}!
        
Welcome to {html.bold("Crypto Helper")} bot!
        """,
        reply_markup=keyboard,
    )
