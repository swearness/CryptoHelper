from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

def get_token() -> str:
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не найден в .env")

    return BOT_TOKEN