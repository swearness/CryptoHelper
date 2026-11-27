from aiogram import F, Router, html
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.main_menu import keyboard
from services.user_service import get_user

router = Router()


@router.callback_query(F.data == "show_profile")
async def show_profile(callback: CallbackQuery, session: AsyncSession) -> None:
    await callback.answer()

    user = await get_user(session, callback.from_user.id)

    if user is None:
        await callback.answer("User not found", show_alert=True)
        return

    await callback.message.edit_text(
        f"""
        Your profile:

{html.bold("Name")}: {callback.from_user.first_name}
{html.bold("ID")}: {callback.from_user.id}
{html.bold("Fiat currency")}: {user.fiat_currency}
{html.bold("Non-fiat currency")}: {user.non_fiat_currency}
""",
        reply_markup=keyboard,
    )
