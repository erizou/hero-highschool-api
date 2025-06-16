from flask import Flask, jsonify

app = Flask(__name__)

import json

@app.route("/scenario")
def get_scenario():
    with open("scenario.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

import os
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
