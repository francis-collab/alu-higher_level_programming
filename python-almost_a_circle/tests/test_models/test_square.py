#!/usr/bin/python3
"""Test cases for Square class"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_attributes(self):
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_area(self):
        s1 = Square(10)
        self.assertEqual(s1.area(), 100)

if __name__ == '__main__':
    unittest.main()
