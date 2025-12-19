import time
import json
import random

SETTINGS_FILE = "../settings.json"
COOLDOWN_SECONDS = 180  # 3 minutes per pair

last_signal_time = {}

def load_settings():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def send_signal(pair, timeframe, direction):
    print(f"📢 Signal | {pair} | {timeframe} | {direction}")

def calculate_signal(pair):
    """
    Strategy Logic (EMA + RSI simulation for now)
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

    now = time.time()

    for pair in pairs:
        last_time = last_signal_time.get(pair, 0)

        # Cooldown check
        if now - last_time < COOLDOWN_SECONDS:
            continue

        signal = calculate_signal(pair)
        if signal:
            send_signal(pair, timeframe, signal)
            last_signal_time[pair] = now

    time.sleep(60)
