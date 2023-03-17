import gettext
import sys
import os
from colorama import Fore, Style


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


# Lista de mensajes admitidos
available_languages = ["es", "en", "jp", "fr"]

# Mostrar el menú de selección de idioma
# Crea el menu de selección
print(Fore.LIGHTCYAN_EX + "+---------------------------+")
print(" "*5 + "Select a language: ")
print("+---------------------------+" + Style.RESET_ALL)
lang_code = create_menu(available_languages)

# Guarda el idioma en la variable LANG
# Crea el objeto translation con el idioma a traducir
# Crea una funcion principal definida como "_" que tradusca los textos
LANG = lang_code
t = gettext.translation("base", "locale", languages=[LANG], fallback=True)
_ = t.gettext

# Separa la seccion del idioma
print("\n")
