from aiogram import html
from aiogram.types import Message

from keyboards.main_menu import keyboard


async def show_main_menu(message: Message, first_name: str, edit: bool = False) -> None:
    text = f"""
        👋 Hi, {html.bold(first_name)}!
        
Welcome to {html.bold("Crypto Helper")} bot!
        """

    if edit:
        await message.edit_text(text, reply_markup=keyboard)
    else:
        await message.answer(text, reply_markup=keyboard)
