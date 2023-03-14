# Define el nombre que tendra el BOT de charla
NAME_BOT = "Assistant"

# Aqui se va a definir el nombre de usuario que se usara a lo largo del Chat
NAME_USER = input("Como te llamas?: ")

# Este mensaje es el que inicia la conversacion
WELCOME_MESSAGES = [f"Hola {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"¿Qué tal {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"¿Cómo estás {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"¿Cómo te va {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"¿Qué hay de nuevo {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"Encantado/a de conocerte {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"Mucho gusto {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"Un placer {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"Bienvenido/a {NAME_USER}, ¿en qué te puedo ayudar?",
                    f"Saludos {NAME_USER}, ¿en qué te puedo ayudar?"]

# Esta es una lista de mensajes de despedida que se mostraran en el chat de manera aleatoria al terminal la conversacion
GOODBYE_MESSAGES = ["Ha sido un placer hablar contigo, espero que nos volvamos a ver pronto. ¡Hasta la vista!",
                    "Te agradezco mucho tu tiempo y tu atención, ojalá podamos seguir en contacto. ¡Que tengas un buen día!",
                    "Me encantó conversar contigo, eres una persona muy interesante. Te deseo lo mejor. ¡Nos vemos!",
                    "Gracias por compartir este rato conmigo, me has hecho reír mucho. Cuídate mucho. ¡Adiós!",
                    "Disfruté mucho de nuestra charla, aprendí muchas cosas nuevas. Te mando un abrazo. ¡Hasta pronto!",
                    "Te voy a extrañar mucho, pero sé que nos volveremos a encontrar. Eres un gran amigo/a. ¡Hasta siempre!",
                    "No es un adiós, es un hasta luego. Esta despedida no es el final",
                    "simplemente significa que te extrañaré hasta que nos encontremos de nuevo.",
                    "No quiero decirte adiós, porque sé que nos volveremos a ver. Eres una persona muy especial para mí. ¡Hasta la próxima!",
                    "Te agradezco por todo lo que me has dado, eres una persona increíble. Espero que la vida te sonría. ¡Hasta luego!",
                    "Me duele despedirme de ti, pero sé que es lo mejor. Te quiero mucho y te deseo lo mejor. ¡Adiós!",
                    "Ha sido un honor conocerte, eres una persona muy admirable. Espero que sigas cumpliendo tus sueños. ¡Hasta pronto!",
                    "Te voy a recordar siempre, eres una persona muy importante en mi vida. Gracias por todo lo que hemos vivido. ¡Hasta siempre!",
                    "No es una triste despedida. Volveremos a encontrarnos de nuevo. Sólo en la agonía de la separación es cuando buscamos en las profundidades del amor.",
                    "Las manos que dicen adiós son pájaros que van muriendo lentamente. Te echaré de menos, pero sé que estarás bien. ¡Adiós!", "Cada despedida es un encuentro que queda para más tarde. No te olvides de mí, yo no me olvidaré de ti. ¡Hasta la vista!"]

# Lista de opciones que hay que notificarle al usuario
OPTIONS_HEADER = ["Num", "Referencia", "Funcion"]
# ["Ctrl + Z | Enter", "Con esta combinación de teclas se envia la peticion."]
OPTIONS_BODY = [["stop",
                 "Esta palabra detiene el chat y termina la sesión."],
                ["clean", "Esta palabra borra el contenido de la pantalla y deja el chat listo para recibir nuevos comandos."],
                ["${send_file}", "Esta palabra te permite cargar un archivo desde tu dispositivo\n y usar su contenido como parte del comando. \nPor ejemplo, si quieres enviar un texto\nguardado en un archivo llamado “mensaje.txt”,\npuedes escribir: enviar ${send_file} y seleccionar el archivo \n“mensaje.txt” cuando se te solicite."]]

# Indica las palabras clave que puede aceptar el chat
KEYS = ["${send_file}"]

# Esta variable guarda el numero de preguntas hechas al bot
COUNT = 0

# Indica si se quiere colorear el texto que nos haya dado el chatbot
COLOR_TEXT = True

# Indica si se quiere el efecto typing en la terminal
TYPING_EFFECT = True

# Indica si quieres ver el input modificado con alguna KEY especial
VIEW_NEW_INPUT = True

# Indica si se imprimiran las instrucciones y funciones disponibles en el chatbot
VIEW_INSTRUCCION = True
