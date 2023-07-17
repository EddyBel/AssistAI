class CoreAssistant:
    def __init__(self, ia: str, model: str, apikey: str, context: str) -> None:
        self.name_ia: str = ia
        self.model: str = model
        self.apikey = apikey
        self.ia = None
        self.voice = None
        self.context = context
        self.lastresponse = ""
        self.chat = [{"role": "system", "content": self.context}]

    def load_model(self):
        try:
            if self.name_ia == "ChatGPT":
                from .models.openai import ChatGPT

                self.ia = ChatGPT(self.apikey, self.model)
        except:
            self.ia = None
            print(f"Error loading model {self.name_ia}")

    def get_response_from_model(self, question: str):
        try:
            if self.name_ia.lower() == "chatgpt":
                self.chat.append({"role": "user", "content": question})
                response = self.ia.get_response(context=self.chat)
                self.lastresponse = response
                self.chat.append({"role": "assistant", "content": response})
                return response
            else:
                text = "Model match not found"
                self.lastresponse = text
                return text
        except Exception as error:
            message_error = f"An error occurred while getting the bot's response. \n Error Server: {error}"
            self.lastresponse = message_error
            self.chat.append({"role": "assistant", "content": message_error})
            return message_error

    def create_voice_from_response(self):
        from .lib.voice import Voice
        from .utils.filesmanager import FileManager
        import os

        filemanager = FileManager()
        voice = Voice()
        voice.text_to_spech(self.lastresponse)

        return filemanager.readFileBytes(os.path.join(os.getcwd(), "core/audio.mp3"))

    def create_voice(self, text: str):
        from .lib.voice import Voice
        import os
        from .utils.filesmanager import FileManager

        filemanager = FileManager()
        voice = Voice()
        voice.text_to_spech(text)

        return filemanager.readFileBytes(os.path.join(os.getcwd(), "core/audio.mp3"))

    def reset_conversation(self):
        self.chat = [{"role": "system", "content": self.context}]
