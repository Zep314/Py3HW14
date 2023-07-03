# Погружение в Python (семинары)
# Урок 14. Основы тестирования

import re
import pytest


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


def test_still():
    assert abc_space('qwerty') != 'qwerty', 'Ошибка строки без изменений'

def test_still1():
    assert abc_space('QwErTy') != 'qwerty', 'Ошибка перобразования регистра без потери символов'

def test_still2():
    assert abc_space('Qwerty, asdf! zxcv&') != 'qwerty asdf zxcv', 'Ошибка удаления знаков пунктуации'

def test_still3():
    assert abc_space('Qwerty, привет! zxcv& Пока@') != 'qwerty  zxcv ', 'Ошибка удаления букв другого алфавита, ' \
                                                                        'и всех остальных случаев'


if __name__ == '__main__':
    # print('--== Тестирование функции abc_space() ==--')
    # text = "qqww12e4354 35twrfsadfIOUoasef094"
    # print(f'{text=} {mu7.abc_space(text)=}')
    pytest.main()