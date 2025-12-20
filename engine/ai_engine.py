from datetime import datetime
import pytz

EGYPT = pytz.timezone("Africa/Cairo")

def ai_decision(data):
    trend = data["trend"]
    rsi = data["rsi"]
    confirm = data["confirmation"]

    if not confirm:
        return None

    if trend == "BUY" and rsi < 40:
        direction = "BUY"
    elif trend == "SELL" and rsi > 60:
        direction = "SELL"
    else:
        return None

    now = datetime.now(EGYPT).strftime("%H:%M:%S")

    return {
        "pair": data["pair"],
        "direction": direction,
        "timeframe": data["timeframe"],
        "rsi": rsi,
        "time": now
    }
