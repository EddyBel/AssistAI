from settings import COUNT, GOODBYE_MESSAGES, WELCOME_MESSAGES, OPTIONS_HEADER, OPTIONS_BODY, NAME_USER, NAME_BOT, VIEW_NEW_INPUT, COLOR_TEXT, TYPING_EFFECT, VIEW_INSTRUCCION
from colorama import Fore, Style
from util import clear_console, typingeffect, color_code, bot_indicator, user_indicator, get_random_element_by_array, update_chat, print_table, search_and_replace
from models import openai
import uuid
# import sys

# Crea una instancia para el modelo chatGPT
chatgpt = openai.ChatGPT()

# Limpia la pantalla antes de iniciar la conversacion
clear_console()

# Ejecuta el archivo como un script
if __name__ == "__main__":
    # Crea un nuevo id
    myId = uuid.uuid4()

    # Si la variable que indica que se muestra la tabla es verdadera entonces inicia las instrucciones.
    if VIEW_INSTRUCCION:
        # Agrega a la lista OPTIONS_BODY una sublista con el nombre del usuario y una descripción
        OPTIONS_BODY.append(
            [NAME_USER, "Nombre que usara el bot para referirce a ti."])
        # Agrega a la lista OPTIONS_BODY otra sublista con el nombre del bot y otra descripción
        OPTIONS_BODY.append([NAME_BOT, "Nombre que usara el bot."])
        # Agrega a la lista OPTIONS_BODY una última sublista con el modelo que utiliza el chat y otra descripción
        OPTIONS_BODY.append([chatgpt.model, "Modelo que utiliza el chat."])
        # Al finalizar imprime la tabla con todas las instrucciones
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
            prev_question = question
            # Busca los caracteres especiales asignados en la constante KEYS para modifcar el input, si no se encuentran no haces nada
            question = search_and_replace(question)

            if question != prev_question and VIEW_NEW_INPUT:
                print(f"{Style.DIM}{Fore.LIGHTYELLOW_EX}{question}{Style.RESET_ALL}")

            # Crea diversas validaciones especiales para parar el programa
            if (question == "stop"):
                # Inicia la respuesta del bot de despedida antes de parar el programa
                bot_indicator()
                # Obten un mensaje aleatorio de la lista de mensajes
                goodbye_message = get_random_element_by_array(GOODBYE_MESSAGES)
                # Muestralo en la pantalla
                typingeffect(Fore.LIGHTYELLOW_EX +
                             goodbye_message + Style.RESET_ALL)
                # Para el programa
                break

            # Reinicia el bot para tener una nueva conversación
            elif (question == "clean"):
                clear_console()  # Limpia la consola
                chatgpt.reset_conversation()  # Reinicia la conversación con el chatbot
                myId = uuid.uuid4()  # Genera un nuevo identificador único para el usuario
                bot_indicator()  # Muestra un indicador de que el chatbot está escribiendo
                typingeffect(
                    "De que otro tema interesante te gustaria hablar?\n")  # Escribe con efecto de tipeo una pregunta al usuario
                COUNT = 0  # Reinicia el contador de preguntas
                continue  # Continua con el bucle principal

            # Aumenta uno al contador de preguntas
            COUNT += 1

            # Inicia la respuesta del bot
            bot_indicator()
            # Pregunta al modelo de chatgpt
            response = chatgpt.get_response(question)
            # Si el texto tiene algo que se puede colorear colorealo y retorna la nueva respuesta, solo si en la configuracion se permite.
            response = color_code(response) if COLOR_TEXT else response
            # Muestra la respuesta del bot, y segun la configuracion has el efecto typing o no
            if TYPING_EFFECT:
                typingeffect(response)
            else:
                print(response)
            # # Guarda en un json la conversacion
            update_chat(id=myId, model=chatgpt.model, chat=chatgpt.chat)

        # Muestra el error si asi lo hubo
        except Exception as err:
            response = f"{Fore.RED}Ocurrio un error: {err}{Style.RESET_ALL}\n" if COLOR_TEXT else f"Ocurrio un error: {err}"
            if TYPING_EFFECT:
                typingeffect(response)
            else:
                print(response)
