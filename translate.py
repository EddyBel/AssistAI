import gettext
from colorama import Fore, Style

# Lista de mensajes admitidos
available_languages = ["es", "en", "jp", "fr"]

# Mostrar el menú de selección de idioma
print(Fore.LIGHTCYAN_EX + "+---------------------------+")
print(" "*5 + "Select a language: ")
print("+---------------------------+" + Style.RESET_ALL)
for i, lang in enumerate(available_languages):
    print(f"{i+1}. {lang}")

# Pedir al usuario que seleccione un idioma
selected_lang = input(Fore.LIGHTYELLOW_EX +
                      "\nEnter the number of the selected language: " + Style.RESET_ALL)

# Validar que se seleccione una opción válida
while not (selected_lang.isdigit() and int(selected_lang) in range(1, len(available_languages)+1)):
    # Mostrar un mensaje de error si el valor ingresado no es válido
    print(Fore.RED + "Invalid value. Try again." + Style.RESET_ALL)
    # Pedir al usuario que seleccione un idioma
    selected_lang = input(
        Fore.LIGHTYELLOW_EX + "\nEnter the number of the selected language: " + Style.RESET_ALL)

# Obtener el código de idioma seleccionado
lang_code = available_languages[int(selected_lang)-1]
# Guardar el código de idioma en la variable LANG
LANG = lang_code
# Crear un objeto de traducción usando el archivo .mo correspondiente al idioma
t = gettext.translation("base", "locale", languages=[LANG], fallback=True)
# Crear una función que devuelva la traducción de un mensaje usando el objeto t
_ = t.gettext

# Separa la seccion del idioma
print("\n\n")
