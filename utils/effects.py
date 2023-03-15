from time import sleep
import sys


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
