import asyncio
from .utils.format import replace_reference
from .utils.generate import get_random_element_by_array
from .utils.effects import typingeffect
from .utils.console import (
    user_indicator,
    bot_indicator,
    charge_indicator,
    clean_loader,
    clear_console,
    print_table,
)
from settings import (
    NAME_USER,
    NAME_BOT,
    TYPING_EFFECT,
    IA,
    API_KEY,
    MODEL,
    CONTEXT,
    COLOR_TEXT,
)
from utils.define_text import TEXT
from core.main import CoreAssistant
from CodeChroma import TerminalColors

terminal_colors = TerminalColors()
core_assistant = CoreAssistant(IA, MODEL, API_KEY, CONTEXT)
core_assistant.load_model()


def view(text: str):
    if TYPING_EFFECT:
        if COLOR_TEXT:
            typingeffect(terminal_colors.coloring_text(text))
        else:
            typingeffect(text)
    else:
        if COLOR_TEXT:
            print(terminal_colors.coloring_text(text))
        else:
            print(text)


def response_bot(response: str):
    bot_indicator(NAME_BOT)
    view(response)


async def main():
    """This is the main function that will execute the conversation loop."""

    clear_console()

    print_table(
        ["ID", "REFERENCIA", "FUNCION"],
        [
            ["$stop$", "This command stops the chatbot"],
            ["$clean$", "This command clears the conversation"],
            [NAME_BOT, "Name assigned to the bot"],
            [IA, "Name of the ia to be used as nucleus"],
            [MODEL, "Name of the model to be used"],
        ],
        "INSTRUCCIONS",
    )

    # Get the initial greeting
    gretting = get_random_element_by_array(TEXT["greetings"])
    gretting = replace_reference(gretting, "$NAME_USER$", NAME_USER)
    response_bot(gretting)

    # Starts the conversation loop
    while True:
        user_indicator(NAME_USER)
        question = input()

        if question == "$stop$":
            goodbye = get_random_element_by_array(TEXT["goodbyes"])
            goodbye = replace_reference(goodbye, "$USERNAME$", NAME_USER)
            response_bot(goodbye)
            break

        # Assigns a load effect for the response
        bot_indicator(NAME_BOT)
        loading_task = asyncio.create_task(charge_indicator())
        await asyncio.sleep(2)
        response = core_assistant.get_response_from_model(question=question)
        loading_task.cancel()
        clean_loader()
        view(response)
        core_assistant.create_voice_from_response()


# Execute the final program
asyncio.run(main=main())
