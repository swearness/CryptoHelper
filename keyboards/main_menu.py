from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👤 Profile", callback_data="button_profile")],
        [InlineKeyboardButton(text="⚙ Settings", callback_data="button_settings")],
        [
            InlineKeyboardButton(
                text="💲 Currencies", callback_data="button_currencies"
            ),
            InlineKeyboardButton(text="📆 Tasks", callback_data="button_tasks"),
            InlineKeyboardButton(text="🛒 Shop", callback_data="button_shop"),
        ],
    ]
)
