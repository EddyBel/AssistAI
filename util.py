from time import sleep
from colorama import Fore, Style
from settings import NAME_BOT, NAME_USER
from datetime import datetime
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter
import re
import os
import sys
import random
import json
from rich.table import Table
from rich.console import Console

console = Console()


def clear_console() -> None:
    """Esta funcion limpia la pantalla."""
    if os.name == 'nt':  # si el sistema operativo es Windows
        os.system('cls')  # ejecuta el comando cls
    else:  # si el sistema operativo es Linux o MacOS
        os.system('clear')  # ejecuta el comando clear


def print_table(headers: list, body: list, title: str = "Instrucciones"):
    """Esta funcion imprime una tabla con los datos pasados por parametro

    Args:
        headers (list): Lista de encabezados a utilizar
        body (list): Lista de elementos que tiene la tabla
        title (str, optional): Titulo que tendra la tabla. Defaults to "Instrucciones".
    """
    # Inicializar una variable para contar las filas
    count = 0
    # Crear un objeto de tipo Table con un título
    table = Table(title=title)
    # Recorrer la lista de encabezados y agregar una columna por cada uno
    for head in headers:
        table.add_column(head, justify="center", style="cyan", no_wrap=True)
    # Recorrer la lista de cuerpo y agregar una fila por cada elemento
    for item in body:
        table.add_row(str(count), item[0], item[1], end_section=True)
        # Incrementar el contador en uno
        count += 1
    # Imprimir la tabla en la consola con justificación al centro
    console.print(table, justify="center")
    # Imprimir una línea en blanco
    print()


def color_code(text: str) -> str:
    """Definir una función que va a colorear el código de un texto buscando los caracteres ```{}``` para hacerlo.

    Args:
        text (str): Texto a colorear

    Returns:
        str: Texto con el código coloreado
    """

    # Definir el patrón de búsqueda como una cadena entre comillas invertidas o comillas simples o dobles o dos acentos graves simples o triples
    pattern = r'(```.*?```|\'\'\'.*?\'\'\'|\'[^\n]*?\'|"[^\n]*?"|\'.*?\'|\`[^\n]*?\`|\(.*?\))'

    # Definir una función que recibe una coincidencia como argumento
    def replacement(match):
        # Si la coincidencia empieza y termina con triple comilla o dos acentos graves simples, devolver la cadena coincidente con el color verde y el estilo predeterminado
        if (match.group(1).startswith('```') and match.group(1).endswith('```')) or (match.group(1).startswith("'''\n") and match.group(1).endswith("'''\n")):
            # Obtener el código que se encuentra entre las comillas invertidas
            codigo = match.group(0)[3:-3]
            # Colorear el código usando Pygments
            # Obtener de manera automatica el lenguaje a utilizar
            lang = guess_lexer(codigo)
            # Colorea la sintaxis del código
            resultado = highlight(
                codigo, lang, TerminalFormatter())
            # Devolver el código coloreado entre las comillas invertidas
            return f'```{Fore.LIGHTCYAN_EX}\n{resultado}{Style.RESET_ALL}```'
        # Si la coincidencia empieza y termina con comilla simple o doble, devolver la cadena coincidente con el color amarillo y el estilo predeterminado
        elif (match.group(1).startswith('"') and match.group(1).endswith('"')) or (match.group(1).startswith("'") and match.group(1).endswith("'")) or (match.group(1).startswith("`") and match.group(1).endswith("`")):
            return f'{Fore.LIGHTYELLOW_EX}{match.group(1)}{Style.RESET_ALL}'
        elif (match.group(1).startswith('(') and match.group(1).endswith(')')):
            return f'{Fore.LIGHTBLUE_EX}{match.group(1)}{Style.RESET_ALL}'
        # Si la coincidencia no empieza ni termina con ninguna de las anteriores, devolver la cadena coincidente sin color
        else:
            return match.group(1)

    # Usar la función re.sub() para reemplazar las subcadenas que coinciden con el patrón con el resultado de la función replacement
    # Usar el argumento flags=re.DOTALL para que el patrón coincida con cualquier carácter, incluso los saltos de línea
    return re.sub(pattern, replacement, text, flags=re.DOTALL)


def typingeffect(text: str, time: float = None) -> None:
    """Esta funcion imprime de manera progresiva el texto pasado por parametro

        Args:
            texto (str): Texto a mostrar de manera progresiva
    """

    if time is None:
        length = len(text)
        time = 0.009 if length > 400 else 0.04

    for letter in text:  # recorre cada letra del texto
        sleep(time)
        sys.stdout.write(letter)  # escribe la letra en la salida estándar
        sys.stdout.flush()  # actualiza la salida estándar


def get_random_element_by_array(array: list) -> any:
    """Esta funcion obtiene un elemento aleatorio de un array

    Args:
        array (list): Array a utilizar

    Returns:
        any: Elemento aleatorio
    """
    # Usamos la función random.choice () para elegir un elemento al azar del array
    element = random.choice(array)
    # Devolvemos el elemento elegido
    return element


def update_chat(id: int, model: str, chat: list):
    """Esta funcion guarda los datos obtenidos hasta el momento del chat en un archivo JSON.

    Args:
        id (int): Id de la conversacion
        model (str): Modelo que se esta utilizando para responder preguntas
        chat (list): Lista que contiene la conversacion con el chat
    """

    # Obtener la fecha y hora actual
    date_now = datetime.now()

    # Intentar abrir el archivo JSON que corresponde al id dado
    try:
        with open(f"./conversations/{id}.json", "r") as file:
            # Cargar los datos del archivo en una variable llamada data
            data = json.load(file)

    # Si el archivo no existe, manejar la excepción FileNotFoundError
    except FileNotFoundError:
        # Crear un diccionario llamado data con la información del chat
        data = {
            "id": str(id),  # El id del chat como una cadena
            "model": model,  # El modelo usado para el chat
            # La fecha del chat en formato año-mes-día
            "date": f"{date_now.year}-{date_now.month}-{date_now.day}",
            # La hora del chat en formato hora:minuto:segundo
            "hour": f"{date_now.hour}:{date_now.minute}:{date_now.second}",
            "length": str(len(chat)),  # La longitud del chat como una cadena
            "chat": chat  # La lista del chat
        }

    # Actualizar el campo chat del diccionario data con el parámetro chat
    data["chat"] = chat
    # Actualizar el campo length del diccionario data con la longitud del parámetro chat
    data["length"] = str(len(chat))

    # Abrir el archivo JSON que corresponde al id dado en modo escritura
    with open(f"./conversations/{id}.json", "w") as file:
        # Guardar el diccionario data en el archivo como un objeto JSON
        json.dump(data, file)


def bot_indicator() -> None:
    """Esta funcion imprime la referencia que el bot esta hablando en el char"""
    print(Fore.BLUE + f"@[{NAME_BOT}]" + Style.RESET_ALL)


def user_indicator() -> None:
    """Esta funcion imprime la referencia que el usuario esta hablando en el char"""
    print(Fore.CYAN + f"@[{NAME_USER}]" + Style.RESET_ALL)
