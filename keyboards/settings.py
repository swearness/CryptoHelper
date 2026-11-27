from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⚙ Settings", callback_data="show_settings")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="back:menu")],
    ]
)
