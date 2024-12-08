# chatbot.py

class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm just a bot, but I'm doing fine!",
            "bye": "Goodbye!",
        }

    def respond(self, message):
        return self.responses.get(message.lower(), "I don't understand that.")

if __name__ == "__main__":
    bot = Chatbot()
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {bot.respond(message)}")
