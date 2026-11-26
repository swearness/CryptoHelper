import aiohttp

from config import get_paprica_url


class CryptoAPI:
    def __init__(self) -> None:
        self.session = None

    async def start(self) -> None:
        self.session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10))

    async def close(self) -> None:
        if self.session:
            await self.session.close()

    async def get_coin(self, coin_id: str) -> str:
        url = f"{get_paprica_url()}/tickers/{coin_id}"

        async with self.session.get(url) as resp:
            resp.raise_for_status()
            return await resp.json()
