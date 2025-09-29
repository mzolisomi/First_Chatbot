from flask import Flask, render_template, request, jsonify
from Chatbot import get_bot_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    if user_message:
        bot_response = get_bot_response(user_message)
        return jsonify({"response": str(bot_response)})
    return jsonify({"error": "No message provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
