# Погружение в Python (семинары)
## Урок 14. Основы тестирования

### Задание 1

1. Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
2. Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
   - doctest,
   - unittest,
   - pytest.



### Решение
**Задание 1**

Решение представлено в файлах:
- *homework_doctest.py*
- *homework_unittest.py*
- *homework_pytest.py*

### Результат работы:

#### *homework_doctest.py:*
   
    C:\Work\python\dz3\Py3HW14\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW14/homework_doctest.py
    
    Process finished with exit code 0

#### *homework_unittest.py:*

    C:\Work\python\dz3\Py3HW14\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW14/homework_unittest.py
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK

    Process finished with exit code 0

#### *homework_pytest.py:*

    (venv) PS C:\Work\python\dz3\Py3HW14> pytest homework_pytest.py
    ========================================================================================= test session starts =========================================================================================
    platform win32 -- Python 3.10.5, pytest-7.4.0, pluggy-1.2.0
    rootdir: C:\Work\python\dz3\Py3HW14
    collected 3 items                                                                                                                                                                                      

    homework_pytest.py ...                                                                                                                                                                           [100%] 

    ========================================================================================== 3 passed in 0.02s ========================================================================================== 
    (venv) PS C:\Work\python\dz3\Py3HW14> 
