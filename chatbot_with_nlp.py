# ---------------------------------
# AI CHATBOT WITH BASIC NLP
# ---------------------------------

import re

print("🤖 AI Chatbot (Type 'bye' to exit)")
print("----------------------------------")

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()

def chatbot_response(user_input):
    tokens = preprocess(user_input)

    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"

    elif any(word in tokens for word in ["how", "are", "you"]):
        return "I'm doing great! Thanks for asking 😊"

    elif any(word in tokens for word in ["name"]):
        return "I am a simple AI Chatbot built using Python."

    elif any(word in tokens for word in ["help"]):
        return "I can answer simple questions. Try asking about weather, python, or me!"

    elif any(word in tokens for word in ["python"]):
        return "Python is a popular programming language used in AI, Data Science, and Web Development."

    elif any(word in tokens for word in ["weather"]):
        return "I can't check live weather yet, but I can help you build a weather app!"

    elif any(word in tokens for word in ["bye", "exit", "quit"]):
        return "Goodbye! Have a great day 👋"

    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)
