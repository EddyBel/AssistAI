from colorama import Style, Fore, ansi
from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters import TerminalFormatter
from utils.files import get_file, read_file
from settings import KEYS
import shutil
import re


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
            file_path = get_file()
            # Lee el archivo y obtiene su contenido
            content_file = read_file(file_path)
            # Remplaza el contenido obtenido en el texto
            text = text.replace(key, content_file)

    # Devolver el texto modificado
    return text


def code_detect(code: str) -> (str or None):
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
