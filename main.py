from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear un objeto de chatbot
chat = ChatBot('cctmx')

# Crear un entrenador para el chatbot
trainer = ChatterBotCorpusTrainer(chat)

# Entrenar al chatbot con el corpus de datos predefinido
trainer.train('chatterbot.corpus.spanish')

# Ahora el bot está entrenado y listo para responder
while True:
    # Obtener la entrada del usuario
    peticion = input('Tu: ')
    # Obtener la respuesta del chatbot
    respuesta = chat.get_response(peticion)
    # Imprimir la respuesta del chatbot
    print('Bot:', respuesta)
