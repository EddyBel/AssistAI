from lang import LANG_ES, LANG_EN, LANG_JP
from settings import LANGUAGE

TEXT = None

if LANGUAGE.lower() == "es":
    TEXT = LANG_ES
elif LANGUAGE.lower() == "en":
    TEXT = LANG_EN
elif LANGUAGE.lower() == "jp":
    TEXT = LANG_JP
else:
    TEXT = LANG_EN
