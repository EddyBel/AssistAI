from settings import KEYS
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import json


def save_chat(id: int, model: str, chat: list):
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
