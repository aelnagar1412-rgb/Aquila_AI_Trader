from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  # السماح بـ Cross-Origin Requests من الـ Dashboard

# متغيرات الحالة
bot_status = {"running": False}
current_signal = {
    "pair": "EURUSD",
    "direction": "BUY",
    "timeframe": "5m",
    "live_price": 1.0850,
    "entry_time": "14:30:00",
    "duration": "15m",
    "confidence": 85,
    "quality": "excellent",
    "reason": "EMA Crossover + RSI Oversold"
}

# ============ BOT CONTROL ============
@app.route('/api/bot/status', methods=['GET'])
def get_bot_status():
    return jsonify(bot_status)

@app.route('/api/bot/start', methods=['POST'])
def start_bot():
    bot_status["running"] = True
    return jsonify({"message": "Bot started", "status": bot_status})

@app.route('/api/bot/stop', methods=['POST'])
def stop_bot():
    bot_status["running"] = False
    return jsonify({"message": "Bot stopped", "status": bot_status})

@app.route('/api/bot/restart', methods=['POST'])
def restart_bot():
    bot_status["running"] = True
    return jsonify({"message": "Bot restarted", "status": bot_status})

# ============ SIGNAL ============
@app.route('/api/signal/current', methods=['GET'])
def get_current_signal():
    return jsonify(current_signal)

@app.route('/api/signal/generate', methods=['POST'])
def generate_signal():
    # هنا يتم توليد إشارة جديدة من محرك التحليل
    return jsonify({"message": "Signal generated", "signal": current_signal})

# ============ LIVE PRICE ============
@app.route('/api/price/live', methods=['GET'])
def get_live_price():
    pair = request.args.get('pair', 'EURUSD')
    # هنا يتم جلب السعر من API خارجي (مثل Alpha Vantage, IQFeed, etc)
    return jsonify({"pair": pair, "price": 1.0850, "timestamp": datetime.now().isoformat()})

# ============ MARKET STATUS ============
@app.route('/api/market/status', methods=['GET'])
def get_market_status():
    return jsonify({
        "market": "FOREX",
        "status": "open",
        "session": "London"
    })

# ============ PAIRS MANAGEMENT ============
@app.route('/api/pairs/list', methods=['GET'])
def get_pairs():
    return jsonify({
        "pairs": ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD"]
    })

@app.route('/api/pairs/add', methods=['POST'])
def add_pair():
    data = request.json
    pair = data.get('pair')
    return jsonify({"message": f"Pair {pair} added"})

@app.route('/api/pairs/remove', methods=['POST'])
def remove_pair():
    data = request.json
    pair = data.get('pair')
    return jsonify({"message": f"Pair {pair} removed"})

# ============ PERFORMANCE HISTORY ============
@app.route('/api/performance/history', methods=['GET'])
def get_performance():
    return jsonify({
        "total_signals": 45,
        "excellent": 18,
        "very_good": 15,
        "good": 10,
        "moderate": 2,
        "average_confidence": 82.5
    })

# ============ SETTINGS ============
@app.route('/api/settings/all', methods=['GET'])
def get_settings():
    return jsonify({
        "strategies": {
            "trend": True,
            "momentum": True,
            "breakout": True,
            "mean_reversion": True,
            "time_bias": True
        },
        "confidence_threshold": 75,
        "telegram": {
            "enabled": True,
            "format": "detailed",
            "language": "ar"
        }
    })

@app.route('/api/settings/update', methods=['POST'])
def update_settings():
    data = request.json
    # حفظ الإعدادات في قاعدة البيانات
    return jsonify({"message": "Settings updated", "settings": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
