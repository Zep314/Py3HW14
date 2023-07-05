"""
Класс для работы с факториалом
"""

# Задание №1
# - Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# - Экземпляр должен запоминать последние k значений.
# - Параметр k передаётся при создании экземпляра.
# - Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# Задание №2
# - Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
# Задание №3
# - Создайте класс-генератор.
# - Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# - Если переданы два параметра, считаем step=1.
# - Если передан один параметр, также считаем start=1.


import json


class MyFactorial:
    """
    Класс - факториал, для демонстрации продвинутой работы с ООП
    >>> MyFactorial(7).get_factorial()
    5040
    >>> MyFactorial(5).get_factorial()
    120
    """
    _cache = {}

    def __init__(self, k, file_name='output.json'):
        self.k = k
        self.file_name = file_name
        self._cache = {}  # Кэш для вычисленных ранее значений

    def _factorial(self, k: int) -> int:
        """
        Рекурсивное вычисление факториала с сохранением значений в кэше
        :param k:
        :return: f!(k)
        """
        if k in self._cache.keys():
            return self._cache[k]
        else:
            if k < 0:
                raise ValueError('Факториал от отрицательного числа не считаем!')
            elif k < 2:
                self._cache[k] = 1
                return 1
            else:
                self._cache[k] = k * self._factorial(k - 1)
                return self._cache[k]

    def get_factorial(self):
        """
        Обертка для метода вычисления
        :return:
        """
        return self._factorial(self.k)

    def __str__(self):
        """
        Выводим текущий кэш вычисленных значений факториала
        :return:
        """
        return f'{self._cache}'

    def __enter__(self):
        """
        Задаем менеджер контекста
        :return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        При выходе из менеджера контекста - пишем кэш в json-файл
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        with open(self.file_name, 'w') as f:
            json.dump(self._cache, f, indent=4)


class MyRangeFactorial(MyFactorial):
    """
    Итеративный класс для вычисления факториала
    :param args: start, stop, step
    >>> list(MyRangeFactorial(1,7))
    [1, 2, 6, 24, 120, 720]
    """

    def __init__(self, *args):
        """
        Инициализация с различным количеством аргументов
        :param args:
        """
        self._start = 1
        self._step = 1
        match len(args):
            case 1:
                self._stop = args[0]
            case 2:
                self._start = args[0]
                self._stop = args[1]
            case 3:
                self._start = args[0]
                self._stop = args[1]
                self._step = args[2]
            case _:
                raise ValueError('Ошибка в параметрах')
        if self._start > self._stop:
            raise ValueError('Начальное значение больше конечного')
        self._current = self._start
        super().__init__(self._stop)  # Сразу же вычисляем все значения факториала (они сохранятся в кэше)

    def __str__(self):
        """
        Возвращаем значение факториала последнего члена в итерациях
        :return:
        """
        return f'{super()._factorial(self._stop)}'

    def __iter__(self):
        """
        Необходимо для итерируемого класса
        :return:
        """
        return self

    def __next__(self):
        """
        Один шаг итерации. Последовательно вычисляем значения факториала,
        и контролируем шаг текущей переменной
        :return:
        """
        if self._current < self._stop:
            tmp = super()._factorial(self._current)
            self._current += self._step
            return tmp
        else:
            raise StopIteration
