import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

def format_message(speaker, message):
    return f"{speaker}: {message}"

pairs = [
    ["hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm good, thank you!", "I'm doing well."]],
    ["what's your name", ["I'm a chatbot.", "You can call me ChatGPT."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]],
    ["your age", ["I don't have an age. I'm just a program.", "Age is not applicable to me."]],
    ["who created you", ["I was created by a team of developers.", "The credit goes to the developers who built me."]],
    ["tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "What did one ocean say to the other ocean? Nothing, they just waved."]],
    ["favorite color", ["I don't have a favorite color. I'm just a chatbot.", "Colors are beyond my preferences."]],
    ["where are you from", ["I exist in the digital realm. No specific location.", "I don't have a physical origin."]],
    ["how can you help", ["I can answer questions, provide information, or just chat with you.", "Feel free to ask me anything!"]],
    ["what is the meaning of life", ["The meaning of life is a subjective question. What does it mean to you?", "The answer to that question is a mystery that everyone must unravel for themselves."]],
]

def simple_chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    chat = Chat(pairs, reflections)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = chat.respond(user_input)
        print(format_message("Chatbot", response))

if __name__ == "__main__":
    simple_chatbot()
