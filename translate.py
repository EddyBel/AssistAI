import gettext
import tabulate

# Lista de mensajes admitidos
available_languages = ["es", "en", "jp", "fr"]

# Define las opciones del menú con sus respectivos códigos
menu_options = [("1", "Español"), ("2", "Inglés"), ("3", "Japonés"), ("4", "Francés")]

# Muestra el menú al usuario en forma de tabla
print(tabulate.tabulate(menu_options, headers=["Code", "Lang"], tablefmt="fancy_outline") + "\n")

# Pide al usuario que ingrese el código del idioma elegido
selected_language_code = input("Ingrese el código del idioma deseado: ")

while True:
   try:
        if int(selected_language_code) > len(menu_options) or int(selected_language_code) < 1:
            selected_language_code = input("Ingrese el código del idioma deseado: ")
        else:
            break
   except:
        selected_language_code = input("Ingresa solo numeros validos: ")

# Guarda el idioma en la variable LANG
# Crea el objeto translation con el idioma a traducir
# Crea una funcion principal definida como "_" que tradusca los textos
LANG = available_languages[int(selected_language_code) - 1]
t = gettext.translation("base", "locale", languages=[LANG], fallback=True)
_ = t.gettext