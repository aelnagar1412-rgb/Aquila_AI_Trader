from flask import Flask, render_template, request, redirect
import json

SETTINGS_FILE = "/root/aquila-dashboard/settings.json"

app = Flask(__name__)

def load_settings():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    settings = load_settings()

    if request.method == "POST":
        settings["enabled"] = "enabled" in request.form
        settings["timeframe"] = request.form["timeframe"]
        settings["pairs"] = request.form["pairs"].upper().split(",")
        settings["strategy"] = request.form["strategy"]
        settings["risk"] = request.form["risk"]

        save_settings(settings)
        return redirect("/")

    return render_template("dashboard.html", settings=settings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
