"""
Модуль содержит класс MyMatrix для оперирования матрицами чисел
с возможностью сравнения, сложения, умножения и вывода на печать
"""


class MyMatrixSizeCreateError(Exception):
    """
    Исключение вызывается, когда пытаются создать не прямоугольную матрицу
    """
    pass


class MyMatrixSizeNotMatchError(Exception):
    """
    Исключение вызывается, когда пытаются сложить или сравнить матрицы разного размера
    """
    pass


class MyMatrix:
    """
    Класс для оперирования матрицами чисел
    с возможностью сравнения, сложения, умножения и вывода на печать
    >>> MyMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) + MyMatrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
    [[12, 14, 16], [18, 20, 22], [24, 26, 28]]
    >>> MyMatrix([[1, 1, 0], [1, 0, 2]]) * MyMatrix([[1, 0, 2, 1], [2, 1, 2, 0], [1, 1, 0, 3]])
    [[3, 1, 4, 1], [3, 2, 2, 7]]

    """

    def __init__(self, data):
        """
        Инициализация матрицы - с проверкой на "прямоугольность"
        :param data:
        """
        self.data = data
        row_len = len(data[0])
        for i in range(1, len(data)):
            if len(data[i]) != row_len:
                raise MyMatrixSizeCreateError

    def get_width(self):
        """
        Возвращаем "ширину" матрицы - количество элементов в строке
        :return:
        """
        return len(self.data[0])

    def get_height(self):
        """
        Возвращаем "высоту" матрицы - количество строк
        :return:
        """
        return len(self.data)

    def is_non_negative(self):
        """
        Проверка матрицы на неотрицательность.
        Если есть хотя бы один элемент меньше 0, то возвращаем False, иначе - True
        Метод требуется для операций сравнения матриц
        :return:
        """
        for i in range(self.get_width()):
            for j in range(self.get_height()):
                if self.data[i][j] < 0:
                    return False
        return True

    def __repr__(self):
        """
        Вывод представления матрицы для программистов
        :return:
        """
        return str(self.data)

    def __str__(self):
        """
        Вывод представления матрицы для пользователей
        :return:
        """
        return ''.join(['[' + ', '.join(map(str, self.data[i])) + ']\n' for i in range(self.get_height())])

    def __add__(self, other):
        """
        Сложение двух матриц поэлементно. Матрицы должны быть одинакового размера.
        Иначе - выбрасывается исключение MyMatrixSizeNotMatchError
        :param other:
        :return:
        """
        if self.get_width() != other.get_width() or \
                self.get_height() != other.get_height():
            raise MyMatrixSizeNotMatchError
        return MyMatrix([list(map(sum, zip(*i))) for i in zip(self.data, other.data)])

    def __sub__(self, other):
        """
        Вычитание одной матрицы из другой поэлементно. Матрицы должны быть одинакового размера.
        Иначе - выбрасывается исключение MyMatrixSizeNotMatchError
        :param other:
        :return:
        """
        if self.get_width() != other.get_width() or \
                self.get_height() != other.get_height():
            raise MyMatrixSizeNotMatchError
        return MyMatrix([[self.data[i][j] - other.data[i][j] for j in range
                        (len(self.data[0]))] for i in range(len(self.data))])

    def __eq__(self, other):
        """
        Проверка матриц на равенство. Размеры матриц - неважны
        :param other:
        :return:
        """
        return self.data == other.data

    def __ne__(self, other):
        """
        Проверка матриц на неравенство. Размеры матриц - неважны
        :param other:
        :return:
        """
        return self.data != other.data

    def __gt__(self, other):  # >
        """
        Сравнение матриц. Больше
        Если разность матриц self и other - неотрицательная матрица (is_not_negative)
        то возвращаем True
        :param other:
        :return:
        """
        # Проверка на совпадение размерности матриц будет в операции вычитания
        m = self - other
        return m.is_non_negative()

    def __lt__(self, other):  # <
        """
        Сравнение матриц. Меньше
        Если разность матриц other и self - неотрицательная матрица (is_not_negative)
        то возвращаем True
        :param other:
        :return:
        """
        # Проверка на совпадение размерности матриц будет в операции вычитания
        m = other - self
        return m.is_non_negative()

    def __ge__(self, other):  # <=
        """
        Сравнение матриц. Меньше или равно
        :param other:
        :return:
        """
        return self == other or self < other

    def __le__(self, other):  # >=
        """
        Сравнение матриц. Больше или равно
        :param other:
        :return:
        """
        return self == other or self > other

    def __mul__(self, other):
        """
        Перемножение матриц
        :param other:
        :return:
        """
        if self.get_width() != other.get_height():
            raise MyMatrixSizeNotMatchError
        res = [[None for _ in range(other.get_width())] for __ in range(self.get_height())]
        for i in range(self.get_height()):
            for j in range(other.get_width()):
                res[i][j] = sum(self.data[i][kk] * other.data[kk][j] for kk in range(self.get_width()))
        return MyMatrix(res)
