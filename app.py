from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the BGO Chatbot API!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]

    # Dummy response (replace with OpenAI API logic)
    chatbot_response = f"Chatbot says: {user_message}"

    return jsonify({"response": chatbot_response})

if __name__ == "__main__":
    app.run(debug=True)
