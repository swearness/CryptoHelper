from os import getenv

from dotenv import load_dotenv

load_dotenv()


def get_token() -> str:
    token = getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN doesn't exists in .env")

    return token


def get_database_url() -> str:
    url = getenv("DATABASE_URL")

    if not url:
        raise ValueError("DATABASE_URL doesn't exists!")

    return url
