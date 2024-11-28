#!/usr/bin/python3
"""Test cases for Rectangle class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_attributes(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rectangle_area(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)

if __name__ == '__main__':
    unittest.main()
