import time
import json
import os
from datetime import datetime, timedelta
import pytz

from telegram import send_message
from telegram_control import load_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")

EG_TZ = pytz.timezone("Africa/Cairo")

def egypt_now():
    return datetime.now(EG_TZ)

def calc_expiry(start_time, timeframe):
    minutes = int(timeframe.replace("m", ""))
    return start_time + timedelta(minutes=minutes)

print("🚀 Aquila Engine Started")

last_sent = {}

while True:
    settings = load_settings()

    if not settings.get("enabled", False):
        print("⏸ Bot Disabled - waiting...")
        time.sleep(5)
        continue

    timeframe = settings["timeframe"]
    pairs = settings["pairs"]

    for pair in pairs:
        now = egypt_now()

        # منع تكرار الإشارة لنفس الزوج خلال نفس الدقيقة
        key = f"{pair}_{now.strftime('%Y%m%d%H%M')}"
        if key in last_sent:
            continue
        last_sent[key] = True

        direction = "CALL ⬆️" if now.second % 2 == 0 else "PUT ⬇️"

        entry_time = now
        expiry_time = calc_expiry(entry_time, timeframe)

        message = (
            "🚨 إشارة تداول مؤكدة\n\n"
            f"📊 الزوج: {pair}\n"
            f"⏱ الفريم: {timeframe}\n"
            f"🎯 نوع الصفقة: {direction}\n\n"
            f"🕒 وقت الدخول: {entry_time.strftime('%I:%M:%S %p')} 🇪🇬\n"
            f"⏳ انتهاء الصفقة: {expiry_time.strftime('%I:%M:%S %p')} 🇪🇬\n\n"
            "⚠️ التزم بإدارة رأس المال\n"
            "🤖 Aquila AI Trader"
        )

        send_message(message)
        print(f"✅ Signal sent for {pair}")

        time.sleep(2)

    time.sleep(30)
