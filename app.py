from flask import Flask
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Hello DevOps 🚀")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Production")

@app.route("/")
def home():
    return f"""
    <h1>{APP_NAME}</h1>
    <h2>Environment: {ENVIRONMENT}</h2>
    <h3>Flask + Docker + Kubernetes + ConfigMap</h3>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
