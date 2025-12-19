import requests

BOT_TOKEN = "8570409684:AAEQBhKv0zMZaEXWcoCUGiJsKRspE5JuleM"
CHAT_ID = "818760257"

def send_signal(signal):
    text = f"""
📢 إشارة تداول جديدة

📊 الزوج: {signal['pair']}
⏱ الفريم: {signal['timeframe']}
🚀 الاتجاه: {'صعود' if signal['signal']=='BUY' else 'هبوط'}
    """

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, json=payload)
