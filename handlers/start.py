from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        f"""
        👋 Hi, {html.bold(message.from_user.first_name)}!
        
Welcome to {html.bold("Crypto Helper")} bot!
        """
    )
