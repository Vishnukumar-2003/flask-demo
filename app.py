from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, DevOps! Flask application is running."

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "flask-demo"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)