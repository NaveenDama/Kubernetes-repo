# service1.py
from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Service 1"


@app.route("/service1/")
def hello():
    return "Hello from Service 1!"


@app.route("/service1/call-service2/")
def call_service2():
    response = requests.get("http://service2-service/service2/")
    return f"Service 1 calling Service 2: {response.text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
