from flask import Flask, jsonify
import json
import os

app = Flask(__name__)



@app.route("/scenario")
def get_scenario():
    with open("scenario.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/characotor")
def get_scenario():
    with open("characotor.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

import os
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
