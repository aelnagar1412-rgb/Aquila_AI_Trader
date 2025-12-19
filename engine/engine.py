import json
import time

SETTINGS_PATH = "/root/aquila-dashboard/settings.json"

def load_settings():
    with open(SETTINGS_PATH, "r") as f:
        return json.load(f)

def run_engine():
    print("🚀 Aquila Engine Started")

    while True:
        settings = load_settings()

        if not settings.get("enabled", False):
            print("⏸ Bot Disabled – waiting...")
            time.sleep(5)
            continue

        timeframe = settings.get("timeframe", "1m")
        pairs = settings.get("pairs", [])

        print("✅ Bot Enabled")
        print("⏱ Timeframe:", timeframe)
        print("💱 Pairs:", pairs)

        # هنا مكان الاستراتيجية بعدين
        time.sleep(10)

if __name__ == "__main__":
    run_engine()
