import json


def load_languages(file_name: str):
    with open(file_name, "r") as file:
        return json.load(file)


LANG_ES = load_languages("./lang/es.json")
LANG_EN = load_languages("./lang/en.json")
LANG_JP = load_languages("./lang/jp.json")
