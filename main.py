from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/scenario")
def get_scenario():
    return jsonify({
        "title": "HERO☆ハイスクール",
        "genre": ["アクション", "学園", "SF"]
    })

@app.route("/characters")
def get_characters():
    with open("character.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

# ポート設定（Render向け）
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
