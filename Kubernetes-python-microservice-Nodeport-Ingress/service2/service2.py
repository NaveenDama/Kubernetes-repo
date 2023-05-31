# service2.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Service 2"


@app.route("/service2/")
def hello():
    return "Hello from Service 2!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
