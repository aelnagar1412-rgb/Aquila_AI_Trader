from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("../settings.json", "r") as f:
        settings = json.load(f)

    data = {
        "status": "ON" if settings.get("bot_enabled") else "OFF",
        "timeframe": settings.get("timeframe", "1m"),
        "pairs": ", ".join(settings.get("pairs", [])),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "signals": []
    }

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
