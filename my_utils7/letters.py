import re


def abc_space(text:str) -> str:
    """
    Функция удаляет из строки все символы, кроме букв латинского алфавита и пробелов,
    и возвращаяет строку в нижнем регистре
    :param text:
    :return:
    """
    return re.sub('[^a-z ]', '', text.lower())
