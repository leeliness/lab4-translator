import asyncio
from translator_package import deep_module as tr


async def main():

    text = "Добрий день"

    result = await tr.TransLate(text,"auto","ga")

    print("Translation:", result)

    lang = await tr.LangDetect(text)

    print("Detected:", lang)

    print("Code:", tr.CodeLang("irish"))


asyncio.run(main())