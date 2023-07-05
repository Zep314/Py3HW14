# Погружение в Python (семинары)
# Урок 14. Основы тестирования
# Задание №6
# - На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# - Напишите 3-7 тестов pytest для данного проекта.
# - Используйте фикстуры.

import pytest
import my_utils7 as mu7


@pytest.fixture
def my_user():
    return mu7.MyUser('Ivan Petrov', 1, 3)


def test_name(my_user):
    assert my_user.name == 'Ivan Petrov' , 'Ошибка в имени'


def test_id(my_user):
    assert my_user.id == 1 , 'Ошибка ID'


def test_level(my_user):
    assert my_user.access_level == 3 , 'Ошибка уровня доступа'


if __name__ == '__main__':
    pytest.main()

