import random

def analyze(pair, timeframe, risk):
    trend = random.choice(["BUY", "SELL", "SIDE"])
    rsi = random.randint(20, 80)
    confirmation = random.choice([True, False])

    if trend == "SIDE":
        return None

    if risk == "low" and not confirmation:
        return None

    return {
        "pair": pair,
        "timeframe": timeframe,
        "trend": trend,
        "rsi": rsi,
        "confirmation": confirmation
    }
