# Погружение в Python (семинары)
# Урок 14. Основы тестирования
# - Решить задачи, которые не успели решить на семинаре.
# - Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# - Напишите к ним тесты.
# - 2-5 тестов на задачу в трёх вариантах:
#   - doctest,
#   - unittest,
#   - pytest.

import os

if __name__ == '__main__':
    os.system('python.exe -m doctest my_utils7\\my_math.py')
    os.system('python.exe -m doctest my_utils7\\my_math2.py')
    os.system('python.exe -m doctest my_utils7\\my_matrix.py')
