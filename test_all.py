import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter


class TestCircleFunctions(unittest.TestCase):
    def test_circle_area_positive(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2), 4 * math.pi)

    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_circle_perimeter_positive(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(2), 4 * math.pi)

    def test_circle_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_circle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle_perimeter(-1)


class TestSquareFunctions(unittest.TestCase):
    def test_square_area_positive(self):
        self.assertEqual(square_area(1), 1)
        self.assertEqual(square_area(2), 4)

    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            square_area(-1)

    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(2), 8)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square_perimeter(-1)


if __name__ == "__main__":
    unittest.main()
