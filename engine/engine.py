import time
import json
import random
import requests

SETTINGS_FILE = "../settings.json"

def load_settings():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def send_signal(pair, timeframe, direction):
    print(f"📢 Signal | {pair} | {timeframe} | {direction}")

def calculate_signal(pair):
    """
    PLACEHOLDER for real market data
    Strategy Logic Applied
    """

    ema_50 = random.uniform(1.0, 2.0)
    ema_200 = random.uniform(1.0, 2.0)
    rsi = random.randint(30, 70)

    if ema_50 > ema_200 and 40 <= rsi <= 55:
        return "CALL"

    if ema_50 < ema_200 and 45 <= rsi <= 60:
        return "PUT"

    return None

print("🚀 Aquila Engine Started")

while True:
    settings = load_settings()

    if not settings.get("enabled"):
        print("⏸ Bot Disabled - waiting...")
        time.sleep(5)
        continue

    timeframe = settings.get("timeframe", "1m")
    pairs = settings.get("pairs", [])

    print("✅ Bot Enabled")
    print("⏱ Timeframe:", timeframe)
    print("💱 Pairs:", pairs)

    for pair in pairs:
        signal = calculate_signal(pair)
        if signal:
            send_signal(pair, timeframe, signal)

    time.sleep(60)
