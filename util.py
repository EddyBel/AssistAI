from time import sleep
from colorama import Fore, Style, Back, ansi
from settings import NAME_BOT, NAME_USER, KEYS
from datetime import datetime
from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters import TerminalFormatter
import re
import os
import sys
import random
import json
import shutil
from rich.table import Table
from rich.console import Console
import tkinter as tk
from tkinter import filedialog

# Crea una instancia de la consola para centrar elementos
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


def code_detect(code: str):
    """Esta función recibe un texto y detecta si contiene algún código de programación en él y retorna el código encontrado."""

    # Definir una lista de expresiones regulares para identificar los lenguajes de programación más comunes
    regex = [
        # Buscar las palabras def, print o elif seguidas de un nombre y paréntesis
        (r"(def|print|elif)\s+\w+\(.*\)", "Python"),
        # Buscar las palabras print import o from seguidas de un nombre y paréntesis
        (r"import\s+\w+|from\s+\w+\s+import\s+\w+|print\s*\(", "Python"),
        # Buscar el inicio de un documento HTML o algunas etiquetas comunes
        (r"<!DOCTYPE html>|<div.*?>|<a.*?>|<h[1-6].*?>|<p.*?>|<script.*?>|<img.*?>", "HTML"),
        # Buscar los modificadores de acceso seguidos de class o interface y un nombre
        (r"(public|private|protected)\s+(class|interface)\s+\w+", "Java"),
        # Buscar las palabras fun o println seguidas de un nombre y paréntesis
        (r"(fun|println)\s+\w+\(.*\)", "Kotlin"),
        # Buscar la palabra include seguida de un archivo de cabecera entre <>
        (r"#include\s+<\w+\.h>", "C"),
        # Buscar el uso de librerías o espacios de nombres
        (r"#include\s+<\w+\.h>|using namespace\s+\w+;", "C++"),
        # Buscar las palabras using o namespace seguidas de un nombre y punto y coma
        (r"(using|namespace)\s+\w+;", "C#"),
        # Buscar las funciones console.log, alert o document.write seguidas de un paréntesis
        (r"(console\.log|alert|document\.write)\(", "JavaScript"),
        # Buscar la función console.log o las palabras import o export
        (r"console\.log|import\s+\w+|export\s+\w+", "TypeScript"),
        # Buscar el inicio de un bloque PHP
        (r"<\?php", "PHP"),
        # Buscar la palabra func seguida de un nombre y paréntesis, seguido de una flecha
        (r"func\s+\w+\(.*\)->", "Swift"),
        # Buscar las palabras fun o println seguidas de un nombre y paréntesis
        (r"(fun|println)\s+\w+\(.*\):", "Kotlin"),
        # Buscar el inicio de un script Bash
        (r"\#\!\/bin\/bash", "Bash"),
        (r"\w\s-\w", "Bash"),
        # Buscar el inicio de un documento XML
        (r"<\?xml", "XML"),
        # Buscar una llave abierta seguida de cualquier cosa y una llave cerrada
        (r"\{.*?\}", "JSON"),
        # Buscar la palabra fn o let seguida de un nombre y paréntesis, seguido de una flecha
        (r"(fn|let)\s+\w+\(.*\)", "Rust"),
        (r"println!\(.*\)", "Rust"),
        # Buscar las palabras func o fmt.Println seguidas de un nombre y paréntesis
        (r"(func|fmt\.Println)\s+\w+\(.*\)", "Go"),
        # Buscar la palabra def seguida de un nombre y paréntesis opcionales
        (r"def\s+\w+\s*\(*\)*|puts\s+", "Ruby"),
        # Buscar la palabra def seguida de un nombre y paréntesis, seguido de un igual
        (r"def\s+\w+\(.*\)\s*=", "Scala"),
        # Buscar la palabra function seguida de un nombre y paréntesis
        (r"\bfunction\s+\w+\(.*\)\s*", "Lua"),
        # Buscar las palabras SELECT, FROM o WHERE seguidas de un nombre
        (r"(SELECT|FROM|WHERE)\s+\w+", "SQL"),
        # Busca la estructura de corchetes o de lista para saber si es un código JSON
        (r'\{\n?\s*"\w+":\s*\w+(?:,\n?\s*"\w+":\w+)*\n?\s*\}', "JSON"),
    ]

    # Iterar sobre la lista de expresiones regulares y aplicar cada una al código dado
    for r in regex:
        if re.search(r[0], code):
            return r[1]

    # Si ninguna expresión regular coincide, devolver "No se pudo detectar el lenguaje"
    return None


def color_code(text: str) -> str:
    """Definir una función que va a colorear el código de un texto buscando los caracteres ```{}``` para hacerlo.

    Args:
        text (str): Texto a colorear

    Returns:
        str: Texto con el código coloreado
    """

    # Definir el patrón de búsqueda como una cadena entre comillas invertidas o comillas simples o dobles o dos acentos graves simples o triples
    pattern = r'(```.*?```|\'\'\'.*?\'\'\'|\'[^\n]*?\'|"[^\n]*?"|\'.*?\'|\`[^\n]*?\`|\(.*?\)|https?://\S+)'

    # Definir una función que recibe una coincidencia como argumento
    def replacement(match):
        # Si la coincidencia empieza y termina con triple comilla o dos acentos graves simples, devolver la cadena coincidente con el color verde y el estilo predeterminado
        if (match.group(1).startswith('```') and match.group(1).endswith('```')) or (match.group(1).startswith("'''\n") and match.group(1).endswith("'''\n")):
            # Obtener el código que se encuentra entre las comillas invertidas
            codigo = match.group(0)[3:-3]
            # Colorear el código usando Pygments

            # Obtener el lenguaje del código segun la funcion anteriormente creada
            lang = code_detect(codigo)
            # Valida si la salida no es un nulo
            # Si la salida es nula entonces usa el detector automatico de Pygments
            lexer = get_lexer_by_name(
                lang) if lang != None else guess_lexer(codigo)
            # Colorea la sintaxis del código
            resultado = highlight(
                codigo, lexer, TerminalFormatter())
            # Separadores del código
            # Obten el ancho de la terminal
            width, _ = shutil.get_terminal_size()
            # Crea la linea que va a separar el código del resto del texto
            line = ansi.Style.DIM + Fore.LIGHTBLUE_EX + \
                "+" + "~"*(width - 2) + "+" + Style.RESET_ALL + \
                ansi.Style.RESET_ALL
            # Obtenemos el código coloreado
            code_color = f'\n{Fore.LIGHTGREEN_EX}{lexer.name}{Style.RESET_ALL}\n{Fore.LIGHTCYAN_EX}\n{resultado}{Style.RESET_ALL}'
            # Devolver el código coloreado entre las comillas invertidas
            return code_color
        # Si la coincidencia empieza y termina con comilla simple o doble, devolver la cadena coincidente con el color amarillo y el estilo predeterminado
        elif (match.group(1).startswith('"') and match.group(1).endswith('"')) or (match.group(1).startswith("'") and match.group(1).endswith("'")) or (match.group(1).startswith("`") and match.group(1).endswith("`")):
            return f'{Fore.LIGHTYELLOW_EX}{match.group(1)}{Style.RESET_ALL}'
        # Si la coincidencia empieza por parentesis, devuelve la cadena coloreada de azul
        elif (match.group(1).startswith('(') and match.group(1).endswith(')')):
            return f'{Fore.LIGHTBLUE_EX}{match.group(1)}{Style.RESET_ALL}'
        # Si la coincidencia es una URL, colorearla de azul
        elif match.group(1).startswith('http'):
            return f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{match.group(1)}{Style.RESET_ALL}'
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


def read_file(path: str):
    """Esta funcion lee un archivo con la ruta pasada por parametro

    Args:
        path (str): Ruta donde se encuentra el archivo

    Returns:
        str: Contenido del archivo
    """

    # Abrir el archivo en el path con el modo 'r' (lectura) y la codificación "UTF-8"
    with open(path, 'r', encoding="UTF-8") as file:
        # Leer el contenido del archivo y asignarlo a una variable llamada content
        content = file.read()
    # Devolver el valor de la variable content
    return content


def get_file():
    """Esta funcion habre el explorador de archivos, para poder seleccionar un archivo

    Returns:
        str: Retorna la ruta del archivo seleccionado
    """

    # Crear un objeto de la clase tk.Tk y asignarlo a una variable llamada root
    root = tk.Tk()
    # Ocultar la ventana principal de root
    root.withdraw()
    # Invocar el método askopenfilename de la clase filedialog y asignar el resultado a una variable llamada file_path
    file_path = filedialog.askopenfilename()
    # Devolver el valor de la variable file_path
    return file_path

# Definir la función que busca y reemplaza


def search_and_replace(text: str):
    # Recorrer la lista de keys
    for key in KEYS:
        # Verificar si el texto contiene la key
        if key in text and key == "${send_file}":
            file_path = get_file()
            content_file = read_file(file_path)
            text = text.replace(key, content_file)

    # Devolver el texto modificado
    return text


# ! Aqui se prueban algunas funciones sin requerir al bot
if __name__ == "__main__":
    # * RUTA DEL TEXTO DE PRUEBA "./assets/text.md"
    path = get_file()
    text = read_file(path)
    # text = read_file("./assets/text.md")

    newText = color_code(text=text)
    print(newText)
    # typingeffect(newText)
