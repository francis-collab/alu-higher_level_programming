#!/usr/bin/python3
"""Test cases for Square class"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test the functionality of the Square class"""

    def test_square_attributes(self):
        """Test square attributes"""
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_area(self):
        """Test area calculation of square"""
        s1 = Square(10)
        self.assertEqual(s1.area(), 100)

    def test_square_str(self):
        """Test string representation of square"""
        s1 = Square(10, 2, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")

    def test_square_size_getter(self):
        """Test the size getter"""
        s1 = Square(10)
        self.assertEqual(s1.size, 10)

    def test_square_size_setter(self):
        """Test the size setter"""
        s1 = Square(10)
        s1.size = 20
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.width, 20)
        self.assertEqual(s1.height, 20)

        with self.assertRaises(TypeError):
            s1.size = "10"

        with self.assertRaises(ValueError):
            s1.size = -10

    def test_square_update_args(self):
        """Test update method with *args"""
        s1 = Square(10, 10, 10, 10)
        s1.update(1, 20, 30, 40)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.x, 30)
        self.assertEqual(s1.y, 40)

    def test_square_update_kwargs(self):
        """Test update method with **kwargs"""
        s1 = Square(10, 10, 10, 10)
        s1.update(id=1, size=20, x=30, y=40)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.x, 30)
        self.assertEqual(s1.y, 40)

    def test_square_to_dictionary(self):
        """Test the dictionary representation of square"""
        s1 = Square(10, 2, 1, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})

if __name__ == '__main__':
    unittest.main()
