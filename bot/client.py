import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

# DEMO_FUTURES_URL = "https://demo-fapi.binance.com"
DEMO_FUTURES_URL = "https://testnet.binancefuture.com"

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API keys not found. Set them in .env")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = DEMO_FUTURES_URL

    return client