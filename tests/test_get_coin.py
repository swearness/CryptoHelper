import pytest
from services.api.crypto_api import CryptoAPI


@pytest.mark.asyncio
async def test_get_coin():
    api = CryptoAPI()
    await api.start()

    try:
        crypto = await api.get_coin("btc-bitcoin")

        assert crypto is not None
        assert "quotes" in crypto
        assert "USD" in crypto["quotes"]
        assert crypto["quotes"]["USD"]["price"] > 0

    finally:
        await api.close()
