import json
import os
import asyncio

from translator_package import deep_module as deep


def file_info(filename):

    if not os.path.exists(filename):
        print("File not found")
        return None

    with open(filename,"r",encoding="utf8") as f:

        text = f.read()

    size = os.path.getsize(filename)

    chars = len(text)

    sentences = text.count(".")

    return text,size,chars,sentences


async def main():

    with open("config.json") as f:

        config = json.load(f)

    filename = config["file"]

    lang = config["language"]

    sentences_limit = config["sentences"]

    data = file_info(filename)

    if not data:
        return

    text,size,chars,sentences = data

    print("File:",filename)
    print("Size:",size)
    print("Chars:",chars)
    print("Sentences:",sentences)

    parts = text.split(".")[:sentences_limit]

    text_to_translate = ".".join(parts)

    translated = await deep.TransLate(text_to_translate,"auto",lang)

    if config["output"] == "screen":

        print("\nLanguage:",lang)
        print("Module: deep")
        print("\nTranslated text:\n")
        print(translated)

    else:

        new_file = filename+"_"+lang+".txt"

        with open(new_file,"w",encoding="utf8") as f:

            f.write(translated)

        print("Ok")


asyncio.run(main())