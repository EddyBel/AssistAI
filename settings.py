# Defines the type of interface where the bot will be executed.
INTERFACE = "ui"

# Defines the program language
LANGUAGE = "en"

# Define el nombre que tendra el BOT de charla
NAME_BOT = "Assistant"

# Aqui se va a definir el nombre de usuario que se usara a lo largo del Chat
# Si asignas el nombre desde el inicioe en esta variable no se volvera a preguntar
NAME_USER = "Eduardo"

# Indica el modelo que se usara en el chat
# * ChatGPT
# * GPT4All Pendiente de prueba
IA = "ChatGPT"

# Indica el modelo que utilizara la IA
# * gpt-3.5-turbo
# * Alpaca Pendiente de prueba
MODEL = "gpt-3.5-turbo"

# API KEY de openai, puedes asignar la key en este archivo de configuracion o esperar a que el bot lo pregunta
API_KEY = ""

# Indica el contexto que utilizara la IA para la conversación.
CONTEXT = "Soy {NAME_BOT}, un bot amigable y divertido que responde a todas las preguntas de {NAME_USER}, puedo redactar textos, escribir código, escribir poemas y canciones.<|user|>{NAME_USER}<|endofuser|><|bot|>{NAME_BOT}<|endofbot|>"

# Indica si se quiere colorear el texto que nos haya dado el chatbot
COLOR_TEXT = True

# Indica si se quiere el efecto typing en la terminal
TYPING_EFFECT = True

# Indica si quieres ver el input modificado con alguna KEY especial
VIEW_NEW_INPUT = True

# Indica si se imprimiran las instrucciones y funciones disponibles en el chatbot
VIEW_INSTRUCCION = True

# Indica si el contexto se puede ver
VIEW_CONTEXT = False

# Indica si se quiere que el bot hable
VOICE = False
