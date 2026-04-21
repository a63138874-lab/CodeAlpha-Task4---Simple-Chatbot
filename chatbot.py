def get_reply(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hi!"
    elif "how are you" in message:
        return "I'm fine, thanks!"
    elif "bye" in message or "goodbye" in message:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

def main():
    print("Simple Chatbot: Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)

        if "bye" in user_input.lower().strip():
            break

if __name__ == "__main__":
    main()