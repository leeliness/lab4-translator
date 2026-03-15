import asyncio
from translator_package import gtrans3_module as tr


async def main():

    text = "Добрий день"

    result = await tr.TransLate(text,"auto","en")

    print(result)


asyncio.run(main())