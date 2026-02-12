from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
from flask_cors import CORS
import requests

app = Flask(__name__)

# ENABLE CORS FOR ALL ORIGINS
CORS(app, resources={r"/*": {"origins": "*"}})

# Existing metric counter
REQUEST_COUNT = Counter("request_count", "Total web requests")

# -----------------------------------------------------------
# 1️⃣ CPU USAGE API
# -----------------------------------------------------------
@app.route("/api/cpu")
def api_cpu():
    try:
        response = requests.get("http://prometheus:9090/api/v1/query", params={
            "query": 'rate(container_cpu_usage_seconds_total{id!=""}[1m])'
        })
        data = response.json()

        cpu_value = float(data["data"]["result"][0]["value"][1]) * 100
    except:
        cpu_value = 0

    return jsonify({"cpu": round(cpu_value, 2)})

# -----------------------------------------------------------
# 2️⃣ MEMORY USAGE API
# -----------------------------------------------------------
@app.route("/api/memory")
def api_memory():
    try:
        response = requests.get("http://prometheus:9090/api/v1/query", params={
            "query": 'container_memory_usage_bytes{id!=""}'
        })
        data = response.json()

        mem_bytes = float(data["data"]["result"][0]["value"][1])
    except:
        mem_bytes = 0

    mem_mb = mem_bytes / (1024 * 1024)  # Convert bytes → MB

    return jsonify({"memory": round(mem_mb, 2)})

# -----------------------------------------------------------
# 3️⃣ NETWORK USAGE API
# -----------------------------------------------------------
@app.route("/api/network")
def api_network():
    try:
        rx = requests.get("http://prometheus:9090/api/v1/query", params={
            "query": 'sum(rate(container_network_receive_bytes_total[1m]))'
        }).json()

        tx = requests.get("http://prometheus:9090/api/v1/query", params={
            "query": 'sum(rate(container_network_transmit_bytes_total[1m]))'
        }).json()

        rx_val = float(rx["data"]["result"][0]["value"][1])
        tx_val = float(tx["data"]["result"][0]["value"][1])

    except:
        rx_val = 0
        tx_val = 0

    return jsonify({
        "rx": round(rx_val / 1024, 2),  # Convert to KB
        "tx": round(tx_val / 1024, 2)
    })

# -----------------------------------------------------------
# 4️⃣ AI INSIGHT API (basic logic now, ML model can be added later)
# -----------------------------------------------------------
@app.route("/api/ai")
@app.route("/api/ai")
def api_ai():
    try:
        cpu = requests.get("http://localhost:5000/api/cpu").json()["cpu"]
        memory = requests.get("http://localhost:5000/api/memory").json()["memory"]
        network = requests.get("http://localhost:5000/api/network").json()
        rx = network["rx"]
        tx = network["tx"]
    except:
        return jsonify({"insight": "⚠ Unable to analyze system metrics."})

    if cpu > 80 and memory > 1500:
        insight = "🚨 Critical load detected. Immediate scaling recommended."

    elif cpu > 70:
        insight = "⚠ CPU usage is high. Consider horizontal scaling."

    elif memory > 1500:
        insight = "⚠ Memory usage is unusually high. Monitor for leaks."

    elif rx > 500 or tx > 500:
        insight = "📡 Heavy network traffic detected. Possible spike in requests."

    else:
        insight = "✅ System healthy. All resources operating within safe limits."

    return jsonify({"insight": insight})

# -----------------------------------------------------------
# PROMETHEUS METRICS ENDPOINT (existing)
# -----------------------------------------------------------
@app.route("/metrics")
def metrics():
    REQUEST_COUNT.inc()
    return generate_latest()

# -----------------------------------------------------------
# HOME PAGE (existing)
# -----------------------------------------------------------
@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello from CI/CD + Docker + Prometheus + Grafana!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
