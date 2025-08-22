from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot
chatbot = ChatBot("SupportBot")

# Train chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./FAQ's.yml")

# Chat loop
print("Hi User")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)
