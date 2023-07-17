from CodeChroma import Colors

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
