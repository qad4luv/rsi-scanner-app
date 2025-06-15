import requests
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def run_rsi_scan():
    # TODO: Replace this with real RSI logic
    send_telegram("RSI Scan Triggered!")
    return [{"symbol": "BTCUSDT", "rsi": 81}]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)
