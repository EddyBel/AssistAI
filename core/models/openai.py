import openai


class ChatGPT:
    """Este objeto contiene las funciones basicas para hacer una peticion a chatgpt"""

    def __init__(self, apikey: str = "", model: str = "") -> None:
        # Pedimos al usuario que ingrese su clave de API de OpenAI
        self.api_key = apikey
        # Asigna la apikey a el codigo de openai
        openai.api_key = self.api_key
        # Modelo de openia a utilizar
        self.model = model

    def get_response(self, context: list) -> str:
        """Esta funcion hara la peticion a la api de openai de chatgpt.

        Args:
            text (str): Texto o pregunta de entrada para la api

        Returns:
            str: Respuesta del modelo chatgpt
        """

        # Crea la peticion a la api con el modelo y el texto especificado
        completation = openai.ChatCompletion.create(model=self.model, messages=context)
        # Extrae la respuesta en texto de chatgpt
        response = f"{completation.choices[0].message.content}\n"

        # Retorna la respuesta del modelo
        return response
