import unittest
import rectangle
import square
import circle
import triangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_square_per(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_normal_per(self):
        res = rectangle.perimeter(5, 3)
        self.assertEqual(res, 16)


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_zero_per(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_per(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = circle.area(6)
        self.assertEqual(res, 113.097)

    def test_zero_per(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_per(self):
        res = circle.perimeter(6)
        self.assertEqual(res, 37.699)


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = triangle.area(6, 6)
        self.assertEqual(res, 18)

    def test_zero_per(self):
        res = triangle.perimeter(1, 2, 5)
        self.assertEqual(res, 0)

    def test_normal_per(self):
        res = triangle.perimeter(3, 2, 4)
        self.assertEqual(res, 9)