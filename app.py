import os
import logging
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
chatbot = ChatBot('cctmx')

# Comprobar si el chatbot ya ha sido entrenado previamente
if not os.path.exists('trained.marker'):
    # Configurar el nivel de registro para evitar mensajes de advertencia de ChatterBot
    logging.getLogger('chatterbot').setLevel(logging.ERROR)
    
    # Entrenar el chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.spanish')
    
    # Crear el marcador para indicar que el chatbot ha sido entrenado
    with open('trained.marker', 'w') as f:
        f.write('')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    print("Entre a la funcion SEND")
    user_message = request.json['message']
    bot_response = chatbot.get_response(user_message)
    print("User Message: ", user_message)
    print("Both response: ", bot_response)
    return jsonify({'response': str(bot_response)})

if __name__ == '__main__':
    app.run(debug=True)
