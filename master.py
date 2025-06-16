from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/scenario")
def get_scenario():
    return jsonify({
        "title": "HERO☆ハイスクール",
        "genre": ["アクション", "学園", "SF"]
    })

if __name__ == "__main__":
    app.run()
