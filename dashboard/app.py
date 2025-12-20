from flask import Flask, render_template, redirect
from datetime import datetime
import json

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="../static"
)

def load_settings():
    with open("../settings.json", "r") as f:
        return json.load(f)

@app.route("/")
def dashboard():
    settings = load_settings()
    return render_template(
        "dashboard.html",
        time=datetime.now().strftime("%H:%M:%S %d-%m-%Y"),
        status=settings.get("enabled", False),
        timeframe=settings.get("timeframe", "1m"),
        pairs=settings.get("pairs", []),
        signal=settings.get("last_signal")
    )

@app.route("/start")
def start():
    settings = load_settings()
    settings["enabled"] = True
    with open("../settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    return redirect("/")

@app.route("/stop")
def stop():
    settings = load_settings()
    settings["enabled"] = False
    with open("../settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    return redirect("/")

@app.route("/logout")
def logout():
    return "Logged out"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
