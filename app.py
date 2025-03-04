import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Change to "gpt-4o-mini" if needed
            messages=[{"role": "user", "content": user_message}]
        )

        chatbot_reply = response.choices[0].message.content  # Correct response extraction
        return jsonify({"response": chatbot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle API errors correctly

if __name__ == "__main__":
    app.run(debug=True)
