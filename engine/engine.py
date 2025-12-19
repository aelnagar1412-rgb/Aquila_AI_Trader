import time
import json
from strategy import analyze_market

SETTINGS_PATH = "../settings.json"

def load_settings():
    with open(SETTINGS_PATH, "r") as f:
        return json.load(f)

def run_engine():
    print("🚀 Aquila Engine Started")

    while True:
        settings = load_settings()

        if not settings.get("enabled"):
            print("⏸ Bot Disabled - waiting...")
            time.sleep(3)
            continue

        timeframe = settings.get("timeframe", "1m")
        pairs = settings.get("pairs", [])

        print("✅ Bot Enabled")
        print(f"⏱ Timeframe: {timeframe}")
        print(f"💱 Pairs: {pairs}")

        for pair in pairs:
            signal = analyze_market(pair, timeframe)

            if signal:
                print(f"📢 SIGNAL: {signal['signal']} {signal['pair']} ({signal['timeframe']})")

        time.sleep(10)

if __name__ == "__main__":
    run_engine()
