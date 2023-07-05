"""
Модуль содержит классы для представления геометрических фигур
"""

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

# - Доработайте класс прямоугольник из прошлых семинаров.
# - Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых
# значений (отрицательных).
# - Используйте декораторы свойств.

from math import pi


class MyCircle:
    """
    Класс - окружность
    """
    def __init__(self, radius):
        self.radius = radius

    def circle_len(self) -> float:
        """
        Длина окружности
        :return:
        """
        return 2 * pi * self.radius

    def circle_square(self) -> float:
        """
        Площадь окружности
        :return:
        """
        return pi * self.radius ** 2


class MyRectangle:
    """
    Класс прямоугольник, который может быть квадратом
    """

    __slots__ = ('_height', '_width')

    def __init__(self, *args):
        if len(args) == 1:  # Если один параметр - то это квадрат
            self._width = args[0]
            self._height = args[0]
        else:
            self._width = args[0]
            self._height = args[1]

    def rectangle_len(self):
        """
        Периметр прямоугольника
        :return:
        """
        return 2 * (self._height + self._width)

    def rectangle_square(self):
        """
        Площадь прямоугольника
        :return:
        """
        return self._height * self._width

    def __add__(self, other):
        """
        Сложение двух прямоугольников
        :param other:
        :return:
        """
        new_perimetr = self.rectangle_len() + other.rectangle_len()
        new_width = self._width
        new_height = new_perimetr / 2 - new_width
        return MyRectangle(new_width, new_height)

    def __sub__(self, other):
        """
        Вычитание прямоугольников
        :param other:
        :return:
        """
        new_perimetr = abs(self.rectangle_len() - other.rectangle_len())
        new_width = min(self._width, self._height, other.width, other.height)
        new_height = new_perimetr / 2 - new_width
        return MyRectangle(new_width, new_height)

    def __eq__(self, other):
        """
        Равенство двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() == other.rectangle_square()

    def __ne__(self, other):
        """
        Неравенство двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return not self == other

    def __gt__(self, other):  # >
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() > other.rectangle_square()

    def __lt__(self, other):  # <
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() < other.rectangle_square()

    def __ge__(self, other):  # <=
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() <= other.rectangle_square()

    def __le__(self, other):  # >=
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() >= other.rectangle_square()

    def __repr__(self):
        """
        Представление объекта для программистов
        :return:
        """
        return f'({self._width=}, {self._height=})'

    def __str__(self):
        """
        Представление объекта для пользователей
        :return:
        """
        return f'Прямоугольник {self._width} x {self._height}'

    # Дорабатываем класс - изменяем длину и ширину с проверкой

    @property
    def width(self):
        """
        Геттер ширины
        :return:
        """
        return self._width

    @property
    def height(self):
        """
        Геттер высоты
        :return:
        """
        return self._height

    @width.setter
    def width(self, value):
        """
        Сеттер ширины с проверкой
        :param value:
        :return:
        """
        if value > 0:
            self._width = value
        else:
            raise ValueError('Ширина прямоугольника должна быть больше 0!')

    @height.setter
    def height(self, value):
        """
        Сеттер высоты с проверкой
        :param value:
        :return:
        """
        if value > 0:
            self._height = value
        else:
            raise ValueError('Высота прямоугольника должна быть больше 0!')
