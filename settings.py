from translate import _

# Define el nombre que tendra el BOT de charla
NAME_BOT = "Assistant"

# Aqui se va a definir el nombre de usuario que se usara a lo largo del Chat
# Si asignas el nombre desde el inicioe en esta variable no se volvera a preguntar
NAME_USER = ""

# Indica el modelo que se usara en el chat
# * ChatGPT
# * GPT4All Pendiente de prueba
IA = "ChatGPT"

# Indica el modelo que utilizara la IA
# * gpt-3.5-turbo
# * Alpaca Pendiente de prueba
MODEL = "gpt-3.5-turbo"

# API KEY de openai, puedes asignar la key en este archivo de configuracion o esperar a que el bot lo pregunta
API_KEY = ""

# Indica el contexto que utilizara la IA para la conversación.
CONTEXT = _("Soy {NAME_BOT}, un bot amigable y divertido que responde a todas las preguntas de {NAME_USER}, puedo redactar textos, escribir código, escribir poemas y canciones.<|user|>{NAME_USER}<|endofuser|><|bot|>{NAME_BOT}<|endofbot|>")

# Indica si se quiere colorear el texto que nos haya dado el chatbot
COLOR_TEXT = True

# Indica si se quiere el efecto typing en la terminal
TYPING_EFFECT = True

# Indica si quieres ver el input modificado con alguna KEY especial
VIEW_NEW_INPUT = True

# Indica si se imprimiran las instrucciones y funciones disponibles en el chatbot
VIEW_INSTRUCCION = True

# Indica si el contexto se puede ver
VIEW_CONTEXT = False

# Indica si se quiere que el bot hable
VOICE = False

# Indica las palabras clave que puede aceptar el chat
KEYS = ["${send_file}",
        "${send_img}"]

# Este mensaje es el que inicia la conversacion
WELCOME_MESSAGES = [_("Hola {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("¿Qué tal {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("¿Cómo estás {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("¿Cómo te va {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("¿Qué hay de nuevo {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("Encantado/a de conocerte {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("Mucho gusto {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("Un placer {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("Bienvenido/a {NAME_USER}, ¿en qué te puedo ayudar?"),
                    _("Saludos {NAME_USER}, ¿en qué te puedo ayudar?")]

# Esta es una lista de mensajes de despedida que se mostraran en el chat de manera aleatoria al terminal la conversacion
GOODBYE_MESSAGES = [_("Ha sido un placer hablar contigo, espero que nos volvamos a ver pronto. ¡Hasta la vista!"),
                    _("Te agradezco mucho tu tiempo y tu atención, ojalá podamos seguir en contacto. ¡Que tengas un buen día!"),
                    _("Me encantó conversar contigo, eres una persona muy interesante. Te deseo lo mejor. ¡Nos vemos!"),
                    _("Gracias por compartir este rato conmigo, me has hecho reír mucho. Cuídate mucho. ¡Adiós!"),
                    _("Disfruté mucho de nuestra charla, aprendí muchas cosas nuevas. Te mando un abrazo. ¡Hasta pronto!"),
                    _("Te voy a extrañar mucho, pero sé que nos volveremos a encontrar. Eres un gran amigo/a. ¡Hasta siempre!"),
                    _("No es un adiós, es un hasta luego. Esta despedida no es el final"),
                    _("simplemente significa que te extrañaré hasta que nos encontremos de nuevo."),
                    _("No quiero decirte adiós, porque sé que nos volveremos a ver. Eres una persona muy especial para mí. ¡Hasta la próxima!"),
                    _("Te agradezco por todo lo que me has dado, eres una persona increíble. Espero que la vida te sonría. ¡Hasta luego!"),
                    _("Me duele despedirme de ti, pero sé que es lo mejor. Te quiero mucho y te deseo lo mejor. ¡Adiós!"),
                    _("Ha sido un honor conocerte, eres una persona muy admirable. Espero que sigas cumpliendo tus sueños. ¡Hasta pronto!"),
                    _("Te voy a recordar siempre, eres una persona muy importante en mi vida. Gracias por todo lo que hemos vivido. ¡Hasta siempre!"),
                    _("No es una triste despedida. Volveremos a encontrarnos de nuevo. Sólo en la agonía de la separación es cuando buscamos en las profundidades del amor."),
                    _("Las manos que dicen adiós son pájaros que van muriendo lentamente. Te echaré de menos, pero sé que estarás bien. ¡Adiós!"), _("Cada despedida es un encuentro que queda para más tarde. No te olvides de mí, yo no me olvidaré de ti. ¡Hasta la vista!")]

# Lista de opciones que hay que notificarle al usuario
OPTIONS_HEADER = [_("ID"),
                  _("Referencia"),
                  _("Funcion")]

# Lista que contiene las instrucciones del programa
# * Nombre del usuario y una descripción
# * Nombre del bot y otra descripción
# * Modelo que utiliza el chat y otra descripción
# * IA que utiliza el chat
OPTIONS_BODY = [["stop",
                 _("Este comando detiene el chat y termina la sesión.")],
                ["clean",
                 _("Este comando limpia la conversacion")],
                ["${send_file}",
                 _("Este comando permite cargar el contenido de un archivo en el input.")],
                [NAME_BOT, _("Nombre del bot")],
                [MODEL, _("Modelo del bot")],
                [IA, "IA"]]