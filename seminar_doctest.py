# Погружение в Python (семинары)
# Урок 14. Основы тестирования

import re


def abc_space(text: str) -> str:
    """
    Функция удаляет из строки все символы, кроме букв латинского алфавита и пробелов,
    и возвращаяет строку в нижнем регистре.
    >>> abc_space('qwerty')
    'qwerty'
    >>> abc_space('QwErTy')
    'qwerty'
    >>> abc_space('Qwerty, asdf! zxcv&')
    'qwerty asdf zxcv'
    >>> abc_space('Qwerty, привет! zxcv& Пока@')
    'qwerty  zxcv '
    """
    return re.sub('[^a-z ]', '', text.lower())

if __name__ == '__main__':
    # print('--== Тестирование функции abc_space() ==--')
    # text = "qqww12e4354 35twrfsadfIOUoasef094"
    # print(f'{text=} {mu7.abc_space(text)=}')

    import doctest
    doctest.testmod()
#    doctest.testmod(verbose=True)

