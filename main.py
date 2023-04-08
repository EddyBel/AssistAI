from CodeChroma import Colors, TerminalColors
from utils.format import replace_reference, search_and_replace_commands
from utils.console import clear_console, print_table, bot_indicator, user_indicator, charge_indicator, clean_loader
from utils.effects import typingeffect
from utils.generate import get_random_element_by_array
from utils.files import save_chat
from translate import _
from lib.voice import Voice
from models import openai
import threading
import uuid
import asyncio
import settings
import variables

colors = Colors()
terminal_colors = TerminalColors()
clear_console()


async def print_data(text: str):
    # Inicia a ejecutar la voz si asi se solicita
    if settings.VOICE:
        voice_thread = threading.Thread(target=Voice().speak, args=(text,))
        voice_thread.start()
   
    # Esta function imprime un texto con efecto typing si asi se solicita en la configuración.
    typingeffect(text) if settings.TYPING_EFFECT else print(text)
    
    # Esperar a que termine el subproceso de voz si se inicio
    if settings.VOICE:
        voice_thread.join()   

async def request(text: str):
    # Solicita la respuesta de la API del chatbot
    # Retorna el mensaje de respuesta coloreado si asi se solicita
    response = variables.CHAT.get_response(text=text)
    return terminal_colors.coloring_text(response) if settings.COLOR_TEXT else response


async def main():
    # Asigna el id de la conversación
    # Guardala en una variable global
    variables.ID = uuid.uuid4()
    
    # Pregunta el nombre del usuario al iniciar el programa
    # Guarda el nombre de usuario y preguntalo solo si no existe un nombre
    # Declarar la variable global NAME_USER
    if settings.NAME_USER == "" :
        bot_indicator()
        question_name = _("Como te llamas?")
        settings.NAME_USER = input(f"{question_name}: ")
        
    
    # En esta sección valida que IA vas a utilizar
    # Crea una instancia de la IA seleccionada
    # Si no coincide con ninguna imprime el error y cierra el programa
    if settings.IA == "ChatGPT":
        variables.CHAT = openai.ChatGPT()
    else:
        bot_indicator()
        typingeffect("Ningun modelo fue seleccionado")
        exit()
        
    clear_console()
        
    # Imprime el contexto del chat si asi se solcita
    if settings.VIEW_CONTEXT:
        print(colors.translucent(variables.CHAT.context))
       

    # Imrpime las instrucciones del chatbot si asi se solicita
    if settings.VIEW_INSTRUCCION:
        print_table(settings.OPTIONS_HEADER, settings.OPTIONS_BODY)

    # Inicia la conversacion del bot
    # El bot te dara un mensaje de saludo aleatorio
    # Agreagara el nombre de ususario al mensaje si no lo tiene.
    bot_indicator()
    welcome_mesage = get_random_element_by_array(settings.WELCOME_MESSAGES)
    welcome_mesage = replace_reference(
        welcome_mesage, "{NAME_USER}", settings.NAME_USER)
    await print_data(f"{welcome_mesage}\n")
    # typingeffect(f"{welcome_mesage}\n") if TYPING_EFFECT else print(
    #     f"{welcome_mesage}")

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
            print(colors.translucent(colors.yellow(question))) if question != prev_question and settings.VIEW_NEW_INPUT else ""

            # Crea la validacion que para el programa si la entrada es igual al string "stop"
            # Obten un mensaje aleatorio de despedida
            # Imrpime el mensaje con efecto si asi se solicita
            if question == "stop":
                bot_indicator()
                goodbye_message = get_random_element_by_array(settings.GOODBYE_MESSAGES)
                await print_data(colors.light_yellow(goodbye_message))
                break

            # Reinicia la conversación del bot si asi se solicita con el comando "clean"
            # Crea un nuevo ID
            # Imprime el mensaje de nuevo chat creado
            elif question == "clean":
                clear_console()
                variables.CHAT.reset_conversation()
                variables.ID = uuid.uuid4()
                bot_indicator()
                meessage_new_chat = _("De que otro teme te gustaria hablar?")
                await print_data(f"{meessage_new_chat}\n")
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
            clean_loader()
            await print_data(response_message)
            save_chat(id=variables.ID, model=variables.CHAT.model, chat=variables.CHAT.chat)

        except Exception as error:
            # Si ocurrio un error al ejecutar el script obten ese error (Exception)
            # Calcela la funcion de carga
            # Elimina la impresión de carga
            # Imprime el error obtenido del código
            loading_task.cancel()
            clean_loader()
            msg_error = _("Ocurrio un error:")
            response_color = colors.red(f"{msg_error} {error}") + "\n"
            await print_data(response_color)


if __name__ == "__main__":
    asyncio.run(main())
