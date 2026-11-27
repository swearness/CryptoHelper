from aiogram import Router
from aiogram.types import CallbackQuery

from services.menu_service import show_main_menu

router = Router()


@router.callback_query()
async def test_callback(callback: CallbackQuery):
    if callback.data == "back:menu":
        await show_main_menu(
            callback.message, first_name=callback.from_user.first_name, edit=True
        )

    await callback.answer()
