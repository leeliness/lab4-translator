import sys
from googletrans import Translator


translator = Translator()


def check_version():

    if sys.version_info >= (3,13):

        return "Python version too new for googletrans3"

    return None


async def TransLate(text: str, scr: str, dest: str):

    error = check_version()

    if error:
        return error

    try:

        result = translator.translate(text,src=scr,dest=dest)

        return result.text

    except Exception as e:

        return str(e)