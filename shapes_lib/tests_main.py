import unittest
import math
from functions import calculate_circle_area, calculate_rectagle_area, calculate_triangle_area, is_right_triangle


class TestCircleFunction(unittest.TestCase):

    def test_rectagle(self):
        self.assertEqual(calculate_rectagle_area(5, 5), 5 ** 2)
        self.assertEqual(calculate_rectagle_area(11, 6), 6 * 11)
        self.assertEqual(calculate_rectagle_area(125, 5), 5 ** 4)

    
    def test_negative_rectagle(self):
        with self.assertRaises(ValueError):
            calculate_rectagle_area(0, 5)
            calculate_rectagle_area(0, -5)
            calculate_rectagle_area(5, 0)
            calculate_rectagle_area(0, 0)

    
    def test_is_right_triangle(self):
        self.assertEqual(is_right_triangle(5, 4, 3), True)
        self.assertEqual(is_right_triangle(10, 8, 6), True)
        self.assertEqual(is_right_triangle(8, 15, 17), True)
        self.assertEqual(is_right_triangle(6, 15, 16), False)

    def test_negative_right_triangle(self):
        with self.assertRaises(ValueError):
            is_right_triangle(0, 4, 5)
            is_right_triangle(2, 0, 5)
            is_right_triangle(2, 4, 0)

    def test_triangle(self):
        self.assertEqual(calculate_triangle_area(5, 3, 4), 6)
        self.assertAlmostEqual(calculate_triangle_area(5, 8, 6), 14.981, delta=0.001)
        self.assertAlmostEqual(calculate_triangle_area(7, 8, 10),  27.810, delta=0.001)


    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_triangle_area(-2, 2, 6)
            calculate_triangle_area(0, 2, 1)
            calculate_triangle_area(5, 2, 0)
            calculate_triangle_area(5, 2, 0)



    def test_circle(self):
        self.assertEqual(calculate_circle_area(1), math.pi * 2)
        self.assertEqual(calculate_circle_area(3), math.pi * 6)
        self.assertEqual(calculate_circle_area(2000), math.pi * 4000)
        self.assertEqual(calculate_circle_area(202.31), math.pi * 404.62)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(-2)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(0)



if __name__ == '__main__':
    unittest.main()