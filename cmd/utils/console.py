from CodeChroma import Colors
from rich.table import Table
from rich.console import Console
import os
import asyncio

# Crea una instancia de la consola para centrar elementos, y la instancia para colorear texto
console = Console()
colors = Colors()


def clear_console() -> None:
    """Esta funcion limpia la pantalla."""
    if os.name == "nt":  # si el sistema operativo es Windows
        os.system("cls")  # ejecuta el comando cls
    else:  # si el sistema operativo es Linux o MacOS
        os.system("clear")  # ejecuta el comando clear


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


def bot_indicator(name_bot: str) -> None:
    """Esta funcion imprime la referencia que el bot esta hablando en el char"""
    print(colors.blue(f"@[{name_bot}]"))


def user_indicator(name_user: str) -> None:
    """Esta funcion imprime la referencia que el usuario esta hablando en el char"""
    print(colors.cyan(f"@[{name_user}]"))


async def charge_indicator():
    """Esta funcion crea un efecto de carga en la terminal"""
    bar_chars = ["|", "/", "-", "\\"]
    i = 0
    while True:
        character = bar_chars[i % len(bar_chars)]
        loading_text = colors.translucent(f"Loading {character}")
        print(f"\r{loading_text}", end="", flush=True)
        i += 1
        await asyncio.sleep(0.1)
        print("\r" + " " * 20 + "\r", end="", flush=True)


def clean_loader():
    # Funcion a retornar
    print("\r" + " " * len("Loading ....") + "\r", end="", flush=True)
