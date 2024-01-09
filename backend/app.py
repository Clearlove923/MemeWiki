import json
from flask import Flask, request

app = Flask(__name__)

def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(message, code=404):
    return json.dumps({"error": message}), code

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!"
# Item Routes

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)