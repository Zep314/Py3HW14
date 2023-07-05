# Погружение в Python (семинары)
# Урок 14. Основы тестирования
# - Решить задачи, которые не успели решить на семинаре.
# - Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# - Напишите к ним тесты.
# - 2-5 тестов на задачу в трёх вариантах:
#   - doctest,
#   - unittest,
#   - pytest.

import pytest
import my_utils7 as mu7


@pytest.fixture
def my_matrix1():
    return mu7.MyMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


@pytest.fixture
def my_matrix2():
    return mu7.MyMatrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])


def test_find_root():
    assert mu7.find_roots(1, -1, 1) == ((0.5, -0.8660254037844386), (0.5, 0.8660254037844386)), \
        'Ошибка вычисления квадратного уравнения'
    assert mu7.find_roots(1, 0, 0) == 0, \
        'Ошибка вычисления квадратного уравнения'


def test_factorial():
    assert mu7.MyFactorial(7).get_factorial() == 5040, 'Ошибка вычисления факториала'
    assert list(mu7.MyRangeFactorial(7)) == [1, 2, 6, 24, 120, 720], 'Ошибка вычисления факториала'


def test_matrix(my_matrix1, my_matrix2):
    assert isinstance(mu7.MyMatrix([[1]]) + mu7.MyMatrix([[1]]), mu7.MyMatrix), 'Ошибка возвращаемого типа'

    assert my_matrix1 + my_matrix2 == \
           mu7.MyMatrix([[12, 14, 16], [18, 20, 22], [24, 26, 28]]), 'Ошибка сложения матриц'

    assert mu7.MyMatrix([[1, 1, 0], [1, 0, 2]]) * \
           mu7.MyMatrix([[1, 0, 2, 1], [2, 1, 2, 0], [1, 1, 0, 3]]) == \
           mu7.MyMatrix([[3, 1, 4, 1], [3, 2, 2, 7]]), 'Ошибка умножения матриц'


if __name__ == '__main__':
    pytest.main()
