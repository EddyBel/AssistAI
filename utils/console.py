import sys
import os
from settings import NAME_BOT, NAME_USER
from colorama import Style, Fore
from rich.table import Table
from rich.console import Console


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


def bot_indicator() -> None:
    """Esta funcion imprime la referencia que el bot esta hablando en el char"""
    print(Fore.BLUE + f"@[{NAME_BOT}]" + Style.RESET_ALL)


def user_indicator() -> None:
    """Esta funcion imprime la referencia que el usuario esta hablando en el char"""
    print(Fore.CYAN + f"@[{NAME_USER}]" + Style.RESET_ALL)


def create_menu(options):
    selected_option = 0

    if os.name == "nt":  # Windows
        import msvcrt

        while True:
            # Print the menu options
            for i in range(len(options)):
                if i == selected_option:
                    print("-> " + options[i])
                else:
                    print("   " + options[i])
            # Wait for user input
            key = msvcrt.getch()
            if key == b'\x1b':  # Esc key
                break
            elif key == b'H' or key == b'K':  # Up arrow key
                selected_option = max(0, selected_option - 1)
            elif key == b'P' or key == b'M':  # Down arrow key
                selected_option = min(len(options) - 1, selected_option + 1)
            elif key == b'\r':  # Enter key
                break

            # Move the cursor back to the top of the menu
            sys.stdout.write("\033[F" * len(options))
            sys.stdout.flush()

    else:  # Linux and macOS
        import tty
        import termios

        # Save the terminal settings
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        while True:
            # Print the menu options
            for i in range(len(options)):
                if i == selected_option:
                    print("-> " + options[i])
                else:
                    print("   " + options[i])

            # Wait for user input
            key = ord(sys.stdin.read(1))
            if key == 27:  # Esc key
                break
            elif key == 65:  # Up arrow key
                selected_option = max(0, selected_option - 1)
            elif key == 66:  # Down arrow key
                selected_option = min(len(options) - 1, selected_option + 1)
            elif key == 13:  # Enter key
                break

            # Move the cursor back to the top of the menu
            sys.stdout.write("\033[F" * len(options))
            sys.stdout.flush()

        # Restore the terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    return selected_option
