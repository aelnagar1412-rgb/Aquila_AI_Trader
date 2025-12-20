from flask import Flask, render_template
import json
from datetime import datetime
import pytz
import os

app = Flask(__name__)

DATA_FILE = "../data/signals.json"

def load_signals():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

@app.route("/")
def dashboard():
    tz = pytz.timezone("Africa/Cairo")
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    signals = load_signals()
    return render_template(
        "dashboard.html",
        signals=signals,
        time=now
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
