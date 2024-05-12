from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chat = ChatBot("anonymous")
trainer = ChatterBotCorpusTrainer(chat)
trainer.train("chatterbot.corpus.spanish.greetings")