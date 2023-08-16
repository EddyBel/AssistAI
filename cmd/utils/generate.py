import random


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
