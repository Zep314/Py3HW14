"""
Математический модуль
Модуль не менял. Взял из прошлой домашней работы
"""


def find_roots(a, b, c):
    """
    Вычисление корней квадратного уравнения ax^2+bx+c=0
    >>> find_roots(1, -1, 1)
    ((0.5, -0.8660254037844386), (0.5, 0.8660254037844386))
    >>> find_roots(1, 1, 1)
    ((-0.5, -0.8660254037844386), (-0.5, 0.8660254037844386))
    >>> find_roots(1, 0, 0)
    0.0
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:  # мнимые корни
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        return (real_part, -imaginary_part), (real_part, imaginary_part)
    elif discriminant == 0:  # один действительный корень
        return -b / (2 * a)
    else:  # два действительных корня
        return ((-b - discriminant ** 0.5) / 2 * a,
                (-b + discriminant ** 0.5) / 2 * a,
                )
