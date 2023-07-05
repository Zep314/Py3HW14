# Погружение в Python (семинары)
# Урок 14. Основы тестирования
# Задание №5
# - На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# - Напишите 3-7 тестов unittest для данного класса.


import unittest
import my_utils7 as mu7


class TestAbcSpace(unittest.TestCase):
    def test_method_square(self):
        self.assertEqual(mu7.MyRectangle(1, 1).rectangle_square(), 1, 'Ошибка вычисления площади')
        self.assertEqual(mu7.MyRectangle(3, 3).rectangle_square(), 3 ** 2, 'Ошибка вычисления площади')

    def test_method_perimetr(self):
        self.assertEqual(mu7.MyRectangle(2).rectangle_len(), 2 * 4, 'Ошибка вычисления периметра')
        self.assertEqual(mu7.MyRectangle(6, 3).rectangle_len(), (6 + 3) * 2, 'Ошибка вычисления периметра')

    def test_add_rectangles(self):
        self.assertIsInstance(mu7.MyRectangle(3) + mu7.MyRectangle(3), mu7.MyRectangle, 'Возвращаемый объект '
                                                                                              'не MyRectangle')
        self.assertEqual((mu7.MyRectangle(3) + mu7.MyRectangle(3)).rectangle_len(),
                         mu7.MyRectangle(3).rectangle_len() + mu7.MyRectangle(3).rectangle_len(),
                         'Ошибка сложения прямоугольников по периметру')


if __name__ == '__main__':
    unittest.main()
