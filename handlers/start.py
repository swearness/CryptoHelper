from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        f"""
        👋 Hi, {html.bold(message.from_user.first_name)}!
        
Welcome to {html.bold('Crypto Helper')} bot!
        """
    )