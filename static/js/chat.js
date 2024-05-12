document.addEventListener("DOMContentLoaded", function() {
    const messageBar = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const messageBox = document.querySelector(".message-box");
  
    function sendMessage() {
      const userTypedMessage = messageBar.value.trim(); // Eliminar espacios en blanco al inicio y al final del mensaje
  
      if (userTypedMessage) {
        messageBar.value = "";
  
        const userMessageHTML =
          `<div class="chat message">
            <img src="static/img/user.png">
            <span>${userTypedMessage}</span>
          </div>`;
  
        messageBox.insertAdjacentHTML("beforeend", userMessageHTML);
  
        fetch('/send-message', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: userTypedMessage }),
        })
        .then(response => response.json())
        .then(data => {
          const chatBotResponseHTML =
            `<div class="chat response">
              <img src="static/img/chatbot.png">
              <span>${data.response}</span>
            </div>`;
          messageBox.insertAdjacentHTML("beforeend", chatBotResponseHTML);
        })
        .catch(error => {
          console.error('Error sending message:', error);
        });
      }
    }
  
    // Event listener para el evento "click" en el botón de enviar
    sendBtn.addEventListener("click", sendMessage);
  
    // Event listener para el evento "keypress" en el campo de entrada
    messageBar.addEventListener("keypress", function(event) {
      // Verificar si la tecla presionada es "Enter" (código 13)
      if (event.keyCode === 13) {
        sendMessage();
      }
    });
  });
  