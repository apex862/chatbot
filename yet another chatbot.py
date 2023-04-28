# Import the ChatBot class from chatterbot
from chatterbot import ChatBot
from chatterbot_corpus import corpus

# Create a new instance of a ChatBot
chatbot = ChatBot(
    "ze guy",
    # Use a predefined logic adapter to choose a response
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    # Use a predefined corpus of conversations as the training data
    database_uri="sqlite:///database.db"
)

# Train the chatbot based on the corpus data
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

# Get a response from the chatbot for some input

print('bot: ', chatbot.get_response(input('YOU>')))