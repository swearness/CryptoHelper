from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👤 Profile", callback_data="show_profile")],
        [
            InlineKeyboardButton(
                text="💲 Currencies", callback_data="button_currencies"
            ),
            InlineKeyboardButton(text="📆 Tasks", callback_data="show_tasks"),
            InlineKeyboardButton(text="🛒 Shop", callback_data="show_shop"),
        ],
    ]
)
