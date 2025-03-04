import streamlit as st
import requests

# Set up the title
st.title("💬 Chatbot with OpenAI")

# Input box for user message
user_input = st.text_input("You:", "")

# Button to send the message
if st.button("Send"):
    if user_input.strip():
        # Send request to Flask backend
        response = requests.post(
            "http://127.0.0.1:5000/chat",
            json={"message": user_input},
        )

        # Display chatbot response
        if response.status_code == 200:
            bot_response = response.json().get("response", "No response received")
            st.text_area("Chatbot:", value=bot_response, height=100)
        else:
            st.error("Error: Unable to communicate with the chatbot.")
