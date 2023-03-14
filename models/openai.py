from settings import NAME_USER, NAME_BOT
import openai


class ChatGPT:
    """Este objeto contiene las funciones basicas para hacer una peticion a chatgpt"""

    def __init__(self) -> None:
        # Pedimos al usuario que ingrese su clave de API de OpenAI
        self.api_key = input("Por favor, ingresa tu clave de API de OpenAI: ")
        # Asigna la apikey a el codigo de openai
        openai.api_key = self.api_key
        # Modelo de openia a utilizar
        self.model = "gpt-3.5-turbo"
        # Aqui se almacena la conversacion del chat
        # Agregamos el token <|system|> al inicio del texto de entrada con el contexto que queremos darle al bot
        # Usamos el token <|user|> para indicar el nombre del usuario y el token <|bot|> para indicar el nombre del bot
        self.chat = [{
            "role": "system", "content": f"Soy {NAME_BOT}, un bot amigable y divertido que responde a todas las preguntas de {NAME_USER}, puedo redactar textos, escribir código, escribir poemas y canciones además que normalmente hablo español.<|user|>{NAME_USER}<|endofuser|><|bot|>{NAME_BOT}<|endofbot|>"}]

    def get_response(self, text: str) -> str:
        """Esta funcion hara la peticion a la api de openai de chatgpt.

        Args:
            text (str): Texto o pregunta de entrada para la api

        Returns:
            str: Respuesta del modelo chatgpt
        """
        # Al chat guardado agrega la pregunta del usuario
        self.chat.append({"role": "user", "content": text})

        # Crea la peticion a la api con el modelo y el texto especificado
        completation = openai.ChatCompletion.create(
            model=self.model, messages=self.chat)
        # Extrae la respuesta en texto de chatgpt
        response = f"{completation.choices[0].message.content}\n"

        # Agrega la respuesta del modelo a la conversacion
        self.chat.append({"role": "assistant", "content": response})

        # Retorna la respuesta del modelo
        return response

    def reset_conversation(self):
        # Regresamos el chat con la instruccion base para iniciar una nueva conversación.
        self.chat = [{
            "role": "system", "content": f"Soy {NAME_BOT}, un bot amigable y divertido que responde a todas las preguntas de {NAME_USER}, puedo redactar textos, escribir código, escribir poemas y canciones además que normalmente hablo español.<|user|>{NAME_USER}<|endofuser|><|bot|>{NAME_BOT}<|endofbot|>"}]
