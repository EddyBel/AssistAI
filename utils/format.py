from CodeChroma import Colors
from utils.files import get_file, read_file
from settings import KEYS
import climage

colors = Colors()


def replace_reference(text: str, reference: str, replacement: str) -> str:
    """
    Busca la referencia en el texto y la reemplaza por la cadena de reemplazo.

    Args:
    text (str): El texto donde se buscará la referencia.
    reference (str): La referencia que se quiere reemplazar, debe ir entre llaves y comenzar con un signo de dólar ($), por ejemplo "${NOMBRE}".
    replacement (str): La cadena de texto que se usará para reemplazar la referencia.

    Returns:
    str: El texto resultante con la referencia reemplazada por la cadena de reemplazo, o el texto original si la referencia no se encuentra en el texto.
    """

    return text.replace(reference, replacement) if reference in text else text


def search_and_replace_commands(text: str) -> str:
    # Recorrer la lista de keys
    for key in KEYS:
        # Verificar si el texto contiene la key
        if key in text and key == "${send_file}":
            # Obten la ruta del archivo con el explorador de archivos del sistema
            # Lee el archivo y obtiene su contenido
            # Remplaza el contenido obtenido en el texto
            file_path = get_file()
            content_file = f"\n{read_file(file_path)}"
            text = f"\n{text.replace(key, content_file)}"
        
        elif key in text and key == "${send_img}":
            # Obten la ruta del archivo con el explorador de archivos del sistema
            # Lee el archivo y obtiene su contenido en este caso convierte la imagen
            file_path = get_file()
            img_encoding = f"\n{climage.convert(file_path, is_unicode=True, width=100)}"
            text = f"\n{text.replace(key, img_encoding)}"
           

    # Devolver el texto modificado
    return text