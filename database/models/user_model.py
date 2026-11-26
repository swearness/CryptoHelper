from decimal import Decimal

from sqlalchemy import BigInteger, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    fiat_currency: Mapped[str] = mapped_column(
        String(100),
        default="BTC"
    )

    non_fiat_currency: Mapped[str | None] = mapped_column(
        String(100),
        default="USD"
    )

    balance: Mapped[Decimal] = mapped_column(
        Numeric(20, 8),
        default=Decimal("0")
    )