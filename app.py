from flask import Flask
import pybdf

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World - GitHub - pybdf!"
