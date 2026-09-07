from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
REGISTRY = {}

@app.route("/register", methods=["POST"])
def register():
    d = request.json
    REGISTRY[d["sid"]] = {
        "ip": d["ip"],
        "pwd": d["pwd"],
        "exp": datetime.now() + timedelta(hours=24)
    }
    return jsonify({"status": "OK", "sid": d["sid"]})

@app.route("/find/<sid>", methods=["GET"])
def find(sid):
    if sid in REGISTRY and REGISTRY[sid]["exp"] > datetime.now():
        return jsonify({"found": True, "ip": REGISTRY[sid]["ip"]})
    return jsonify({"found": False})

@app.route("/", methods=["GET"])
def home():
    return "✅ SIM Lookup Server — ONLINE!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
