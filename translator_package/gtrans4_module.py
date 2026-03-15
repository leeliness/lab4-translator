from googletrans import Translator, LANGUAGES

translator = Translator()


async def TransLate(text: str, scr: str, dest: str) -> str:

    try:

        result = await translator.translate(text, src=scr, dest=dest)

        return result.text

    except Exception as e:

        return str(e)


async def LangDetect(text: str, set: str = "all") -> str:

    try:

        result = await translator.detect(text)

        if set == "lang":
            return result.lang

        elif set == "confidence":
            return str(result.confidence)

        else:
            return f"{result.lang} {result.confidence}"

    except Exception as e:

        return str(e)


def CodeLang(lang: str) -> str:

    for code, name in LANGUAGES.items():

        if lang.lower() == name.lower():
            return code

        if lang.lower() == code.lower():
            return name

    return "Language not found"


async def LanguageList(out="screen", text=None):

    try:

        print(f"{'N':<3}{'Language':<20}{'ISO-639':<10}{'Text'}")

        i = 1

        for code, name in LANGUAGES.items():

            if text:

                result = await translator.translate(text, dest=code)

                print(f"{i:<3}{name:<20}{code:<10}{result.text}")

            else:

                print(f"{i:<3}{name:<20}{code}")

            i += 1

        return "Ok"

    except Exception as e:

        return str(e)