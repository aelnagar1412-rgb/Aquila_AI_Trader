from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

SETTINGS_FILE = "settings.json"

def load_settings():
    try:
        with open(SETTINGS_FILE) as f:
            return json.load(f)
    except:
        return {
            "enabled": False,
            "timeframe": "1m",
            "pairs": ["EURUSD", "EURJPY", "EURGBP", "AUDCAD", "USDJPY"]
        }

def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    settings = load_settings()

    if request.method == "POST":
        settings["enabled"] = "enabled" in request.form
        settings["timeframe"] = request.form.get("timeframe", "1m")
        settings["pairs"] = request.form.get("pairs", "").split(",")
        save_settings(settings)
        return redirect("/")

    return render_template("dashboard.html", settings=settings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
