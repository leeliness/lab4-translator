import asyncio
from translator_package import gtrans4_module as tr


async def main():

    text = "Добрий день"

    result = await tr.TransLate(text, "auto", "en")

    print("Translation:", result)

    lang = await tr.LangDetect(text)

    print("Detected:", lang)

    print(tr.CodeLang("english"))

    await tr.LanguageList("screen", text)


asyncio.run(main())