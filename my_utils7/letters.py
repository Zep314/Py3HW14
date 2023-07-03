import re


def abc_space(text: str) -> str:
    """
    Функция удаляет из строки все символы, кроме букв латинского алфавита и пробелов,
    и возвращаяет строку в нижнем регистре.
>>> abc_space('pwefpoiPHPUHQWE01-234j0dqdhnxp9341r 14r80d1xx 0841')
'pwefpoiphpuhqwejdqdhnxpr rdxx '
>>> abc_space('frwe wepoi2134-0k41{m{im#YUG#9832ebp`13~)#nnp1d 1381 3wws')
'frwe wepoikmimyugebpnnpd  wws1'
    """
    return re.sub('[^a-z ]', '', text.lower())
