from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user_model import User


async def register_user(
    session: AsyncSession,
    user_id: int,
    username: str | None
):
    user = await session.get(User, user_id)

    if user:
        return user

    user = User(
        id=user_id,
        username=username,
        fiat_currency="BTC",
        non_fiat_currency="USD",
        balance=Decimal("0")
    )

    session.add(user)
    await session.commit()

    return user


async def get_user(
        session: AsyncSession,
        user_id: int
):
    user = await session.get(User, user_id)

    if user:
        return user
    else:
        return "User not found"