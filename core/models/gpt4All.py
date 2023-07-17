from nomic.gpt4all import GPT4All

# ! TODO Aun se encuentra en proceso de prueba
# ! Instala nomic con pip install nomic

class GPT4ALL:
    
    def __init__(self) -> None:
        # Modelo utilizado
        self.model = "Alpaca"
        # Aqui se almacena la conversacion del chat
        self.context = "Context not create"
        # Crea la estructura del chat
        self.chat = [{
            "role": "system", "content": self.context}]

        
    def get_response(self, text: str) -> str:
        m = GPT4All()
        m.open()
        
        if self.hardware == "CPU":
            return m.prompt(text)
            
        elif self.hardware == "GPU":
            config = {'num_beams': 2,
                      'min_new_tokens': 10,
                      'max_length': 100,
                      'repetition_penalty': 2.0}
            return m.generate(text, config)
            

    def reset_conversation(self):
        # Regresamos el chat con la instruccion base para iniciar una nueva conversación.
        self.chat = [{
            "role": "system", "content": self.context}]