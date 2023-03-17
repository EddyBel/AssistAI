from settings import NAME_BOT, NAME_USER
from colorama import Style, Fore
from rich.table import Table
from rich.console import Console
from colorama import Style
import sys
import os
import asyncio

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
    count = 0
    table = Table(title=title)

    for head in headers:
        table.add_column(head, justify="center", style="cyan", no_wrap=True)

    for item in body:
        table.add_row(str(count), item[0], item[1], end_section=True)
        count += 1
    console.print(table, justify="center")
    print()


def bot_indicator() -> None:
    """Esta funcion imprime la referencia que el bot esta hablando en el char"""
    print(Fore.BLUE + f"@[{NAME_BOT}]" + Style.RESET_ALL)


def user_indicator() -> None:
    """Esta funcion imprime la referencia que el usuario esta hablando en el char"""
    print(Fore.CYAN + f"@[{NAME_USER}]" + Style.RESET_ALL)


def create_menu(options: list):
    # Guarda la selección de idioma
    selected_option = 0

    # Identifica el sistema operativo para poder utilizar la funcion (Windows)
    # Crea un bucle infinito que manejara el menu
    # Utiliza las flechas arriba y abajo para moverte en el menu
    if os.name == "nt":
        import msvcrt

        while True:

           # Imprime las opciones dek menu
           # La que coincida con la seleccionada le agregas "->" y si no "  "
            for i in range(len(options)):
                if i == selected_option:
                    print("-> " + options[i])
                else:
                    print("   " + options[i])

           # Captura la entrada del teclado
           # Con ellas maneja la posición de la flecha
           # Si se selecciona la flecha arriba entonces suma a la variable select 1 con el limite maximo de opciones
           # Si se selecciona la flecha abajo entonces resta a la variable select 1 con el limite minimo de opciones
           # Y si la tecla es Enter para el bucle, con la opcion guardada en la variable
            key = msvcrt.getch()
            if key == b'\x1b':
                break
            elif key == b'H' or key == b'K':
                selected_option = max(0, selected_option - 1)
            elif key == b'P' or key == b'M':
                selected_option = min(len(options) - 1, selected_option + 1)
            elif key == b'\r':  # Enter key
                break

            # Mueve el cursor en las diferentes opciones
            sys.stdout.write("\033[F" * len(options))
            sys.stdout.flush()

    # Misma funcion pero para el sistema Linux y MacOS
    else:
        import tty
        import termios

        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        while True:

            for i in range(len(options)):
                if i == selected_option:
                    print("-> " + options[i])
                else:
                    print("   " + options[i])

            key = ord(sys.stdin.read(1))
            if key == 27:
                break
            elif key == 65:
                selected_option = max(0, selected_option - 1)
            elif key == 66:
                selected_option = min(len(options) - 1, selected_option + 1)
            elif key == 13:
                break

            sys.stdout.write("\033[F" * len(options))
            sys.stdout.flush()

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    return options[selected_option]


async def charge_indicator():
    """Esta funcion crea un efecto de carga en la terminal"""
    bar_chars = ["|", "/", "-", "\\"]
    i = 0
    while True:
        character = bar_chars[i % len(bar_chars)]
        print(
            "\r" + f"{Style.DIM}Loading {character}{Style.RESET_ALL}", end="", flush=True)
        i += 1
        await asyncio.sleep(0.1)
        print("\r" + " " * 20 + "\r", end="", flush=True)
