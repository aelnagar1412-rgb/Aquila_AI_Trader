import json
import time
import os

SETTINGS_FILE = "/root/aquila-dashboard/settings.json"

def load_settings():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

print("🚀 Aquila Engine Started")

while True:
    settings = load_settings()

    if not settings["enabled"]:
        print("⏸ Bot Disabled - waiting...")
        time.sleep(5)
        continue

    tf = settings["timeframe"]
    pairs = settings["pairs"]

    print("✅ Bot Enabled")
    print("⏱ Timeframe:", tf)
    print("💱 Pairs:", pairs)

    # هنا لاحقًا هنحط الاستراتيجية
    time.sleep(60)
