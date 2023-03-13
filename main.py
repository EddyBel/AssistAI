from settings import VIEW_INPUT, COUNT, GOODBYE_MESSAGES, WELCOME_MESSAGES, OPTIONS_HEADER, OPTIONS_BODY, NAME_USER, NAME_BOT
from colorama import Fore, Style
from util import clear_console, typingeffect, color_code, bot_indicator, user_indicator, get_random_element_by_array, update_chat, print_table
from models import openai
import uuid
# import sys

chatgpt = openai.ChatGPT()

# Limpia la pantalla antes de iniciar la conversacion
clear_console()

# Ejecuta el archivo como un script
if __name__ == "__main__":
    # Crea un nuevo id
    myId = uuid.uuid4()

    # Define algunas instrucciones y datos que puede utilizar o ver el usuario
    OPTIONS_BODY.append(
        [NAME_USER, "Nombre que usara el bot para referirce a ti."])
    OPTIONS_BODY.append([NAME_BOT, "Nombre que usara el bot."])
    OPTIONS_BODY.append([chatgpt.model, "Modelo que utiliza el chat."])
    print_table(OPTIONS_HEADER, OPTIONS_BODY)

    # Este texto inicia la conversacion
    bot_indicator()
    # Obten un mensaje aleatorio de la lista de saludos
    welcome_mesage = get_random_element_by_array(WELCOME_MESSAGES)
    typingeffect(f"{welcome_mesage}\n")

    # Iniciamos el Loop que ejecutara continuamente la conversacion con el Char
    while True:

        try:
            # Definimos el texto de entrada que queremos enviar a la API de ChatGPT
            user_indicator()
            # Ingresa la entrada del usuario
            question = input()
            # question = sys.stdin.read()

            # Crea diversas validaciones especiales para parar el programa
            if (question == "clear" or question == "stop" or question == "clean"):
                # Inicia la respuesta del bot de despedida antes de parar el programa
                bot_indicator()
                # Obten un mensaje aleatorio de la lista de mensajes
                goodbye_message = get_random_element_by_array(GOODBYE_MESSAGES)
                # Muestralo en la pantalla
                typingeffect(Fore.LIGHTYELLOW_EX +
                             goodbye_message + Style.RESET_ALL)
                # Para el programa
                break

            # Aumenta uno al contador de preguntas
            COUNT += 1

            # Inicia la respuesta del bot
            bot_indicator()
            # Pregunta al modelo de chatgpt
            response = chatgpt.get_response(question)
            # Si el texto tiene algo que se puede colorear colorealo y retorna la nueva respuesta
            response = color_code(response)
            # Muestra la respuesta de la api final
            typingeffect(response)
            # # Guarda en un json la conversacion
            update_chat(id=myId, model=chatgpt.model, chat=chatgpt.chat)

            # Muestra el texto que se uso de entrada si asi se quiere
            if VIEW_INPUT:
                print(Fore.YELLOW + "-------------------------")
                print(f"Input: {question} \n")
                print("-------------------------" + Style.RESET_ALL)

        # Muestra el error si asi lo hubo
        except Exception as err:
            typingeffect(
                Fore.RED + f"Ocurrio un error: {err}" + Style.RESET_ALL + "\n")
