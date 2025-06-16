from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/scenario")
def get_scenario():
    return jsonify({
        "title": "HERO☆ハイスクール",
        "genre": ["アクション", "学園", "SF"]
    })


import os
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
