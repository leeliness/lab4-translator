from deep_translator import GoogleTranslator
from langdetect import detect


async def TransLate(text: str, scr: str, dest: str) -> str:

    try:

        if scr == "auto":
            scr = detect(text)

        result = GoogleTranslator(source=scr, target=dest).translate(text)

        return result

    except Exception as e:

        return str(e)


async def LangDetect(text: str, set: str="all"):

    try:

        lang = detect(text)

        if set == "lang":
            return lang

        elif set == "confidence":
            return "unknown"

        else:
            return lang

    except Exception as e:

        return str(e)


def CodeLang(lang: str):

    languages = GoogleTranslator().get_supported_languages(as_dict=True)

    for name, code in languages.items():

        if lang.lower() == name.lower():
            return code

        if lang.lower() == code:
            return name

    return "Language not found"