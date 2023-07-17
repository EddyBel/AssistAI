import eel
import base64
from settings import MODEL, IA, API_KEY, NAME_BOT, NAME_USER
from core.main import CoreAssistant
from utils.define_text import TEXT
from utils.format import replace_reference
from utils.util import get_random_element_by_array

context = TEXT["context"]
context = replace_reference(context, "$NAME_BOT$", NAME_BOT)
context = replace_reference(context, "$NAME_USER$", NAME_USER)

core_assistant = CoreAssistant(ia=IA, model=MODEL, apikey=API_KEY, context=context)
core_assistant.load_model()

count = 0

eel.init("ui_interface/web")


@eel.expose
def get_info_model():
    return {"model": MODEL, "ia": IA, "name_bot": NAME_BOT, "name_user": NAME_USER}


@eel.expose
def initial_conversation():
    core_assistant.reset_conversation()
    gretting = get_random_element_by_array(TEXT["greetings"])
    gretting = replace_reference(gretting, "$NAME_BOT$", NAME_BOT)
    gretting = replace_reference(gretting, "$NAME_USER$", NAME_USER)

    core_assistant.chat.append({"role": "assistant", "content": gretting})
    return {"conversation": core_assistant.chat, "response": gretting}


@eel.expose
def add_gretting():
    global count
    count += 1
    gretting = get_random_element_by_array(TEXT["greetings"])
    gretting = replace_reference(gretting, "$NAME_BOT$", NAME_BOT)
    gretting = replace_reference(gretting, "$NAME_USER$", NAME_USER)

    if count <= 1:
        core_assistant.chat.append({"role": "assistant", "content": gretting})
        return {"conversation": core_assistant.chat, "response": gretting}
    else:
        return {"conversation": core_assistant.chat, "response": gretting}


@eel.expose
def get_response(question: str):
    response = core_assistant.get_response_from_model(question)
    chat = core_assistant.chat
    return {"conversation": chat, "response": response}


@eel.expose
def get_conversation():
    return core_assistant.chat


@eel.expose
def get_audio(text):
    return core_assistant.create_voice(text)


@eel.expose
def get_audio_from_response():
    audio_bytes = core_assistant.create_voice_from_response()
    return audio_bytes


eel.start("index.html")
