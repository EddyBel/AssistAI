from settings import GOODBYE_MESSAGES, WELCOME_MESSAGES, OPTIONS_HEADER, OPTIONS_BODY, NAME_USER, NAME_BOT, VIEW_NEW_INPUT, COLOR_TEXT, TYPING_EFFECT, VIEW_INSTRUCCION, VIEW_CONTEXT, IA
from colorama import Fore, Style
from utils.format import replace_reference, color_code, search_and_replace_commands
from utils.console import clear_console, print_table, bot_indicator, user_indicator, charge_indicator
from utils.effects import typingeffect
from utils.generate import get_random_element_by_array
from utils.files import save_chat
from translate import _
from models import openai
import uuid
import asyncio

global my_id
chat = None

# En esta sección valida que IA vas a utilizar
# Crea una instancia de la IA seleccionada
# Si no coincide con ninguna imprime el error y cierra el programa
if IA == "ChatGPT":
    chat = openai.ChatGPT()
else:
    bot_indicator()
    typingeffect("Ningun modelo fue seleccionado")
    exit()

clear_console()


def print_data(text: str):
    """Esta function imprime un texto con efecto typing si asi se solicita en la configuración."""
    typingeffect(text) if TYPING_EFFECT else print(text)


async def request(text: str):
    # Solicita la respuesta de la API del chatbot
    # Retorna el mensaje de respuesta coloreado si asi se solicita
    response = chat.get_response(text=text)
    return color_code(response) if COLOR_TEXT else response


async def main():
    # Asigna el id de la conversación
    my_id = uuid.uuid4()

    # Imprime el contexto del chat si asi se solcita
    if VIEW_CONTEXT:
        print(f"{Style.DIM}{chat.context}{Style.RESET_ALL}")

    # Imrpime las instrucciones del chatbot si asi se solicita
    if VIEW_INSTRUCCION:
        print_table(OPTIONS_HEADER, OPTIONS_BODY)

    # Inicia la conversacion del bot
    # El bot te dara un mensaje de saludo aleatorio
    # Agreagara el nombre de ususario al mensaje si no lo tiene.
    bot_indicator()
    welcome_mesage = get_random_element_by_array(WELCOME_MESSAGES)
    welcome_mesage = replace_reference(
        welcome_mesage, "{NAME_USER}", NAME_USER)
    typingeffect(f"{welcome_mesage}\n") if TYPING_EFFECT else print(
        f"{welcome_mesage}")

    # Inicia el bucle de la conversacion
    while True:

        try:
            # Define la entrada del usuario a la conversación
            # Ejecuta alguna funcion extra si asi se marca en el input
            # Imprime el nuevo input resultante si asi se marca en la configuración
            user_indicator()
            question = input()
            prev_question = question
            question = search_and_replace_commands(question)
            print(f"{Style.DIM}{Fore.LIGHTYELLOW_EX}{question}{Style.RESET_ALL}") if question != prev_question and VIEW_NEW_INPUT else ""

            # Crea la validacion que para el programa si la entrada es igual al string "stop"
            # Obten un mensaje aleatorio de despedida
            # Imrpime el mensaje con efecto si asi se solicita
            if question == "stop":
                bot_indicator()
                goodbye_message = get_random_element_by_array(GOODBYE_MESSAGES)
                print_data(
                    f"{Fore.LIGHTYELLOW_EX}{goodbye_message}{Style.RESET_ALL}")
                break

            # Reinicia la conversación del bot si asi se solicita con el comando "clean"
            # Crea un nuevo ID
            # Imprime el mensaje de nuevo chat creado
            elif question == "clean":
                clear_console()
                chat.reset_conversation()
                my_id = uuid.uuid4()
                bot_indicator()
                meessage_new_chat = _("De que otro teme te gustaria hablar?")
                print_data(f"{meessage_new_chat}\n")
                continue

            # Inicia la repuesta del bot solicita desde su API
            # Ejecuta la funcion que muestra un efecto de carga en la terminal
            # Crea la peticion al bot
            # Una vez se tenga la respuesta calcela la funcion que de carga en segundo plano
            # Elimina el efecto e imprime el resultado de la petición
            # Guarda la conversación en un archivo JSON
            bot_indicator()
            loading_task = asyncio.create_task(charge_indicator())
            await asyncio.sleep(2)
            response_message = await request(question)
            loading_task.cancel()
            print("\r" + " " * len("Loading ....") + "\r", end="", flush=True)
            print_data(response_message)
            save_chat(id=my_id, model=chat.model, chat=chat.chat)

        except Exception as error:
            # Si ocurrio un error al ejecutar el script obten ese error (Exception)
            # Calcela la funcion de carga
            # Elimina la impresión de carga
            # Imprime el error obtenido del código
            loading_task.cancel()
            print("\r" + " " * len("Loading ....") + "\r", end="", flush=True)
            msg_error = _("Ocurrio un error:")
            response_color = f"{Fore.RED}{msg_error} {error}{Style.RESET_ALL}\n"
            print_data(response_color)


if __name__ == "__main__":
    asyncio.run(main())
