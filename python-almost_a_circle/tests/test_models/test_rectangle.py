#!/usr/bin/python3
"""Test cases for Rectangle class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test the functionality of the Rectangle class"""

    def setUp(self):
        """Reset number of objects before each test"""
        Rectangle._Base__nb_objects = 0

    def test_rectangle_attributes(self):
        """Test rectangle attributes"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rectangle_area(self):
        """Test area calculation of rectangle"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)

    def test_rectangle_display(self):
        """Test display method of rectangle"""
        import io
        import sys
        r1 = Rectangle(4, 6)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "####\n####\n####\n####\n####\n####\n")

    def test_rectangle_str(self):
        """Test string representation of rectangle"""
        r1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 10/2")

    def test_rectangle_update_args(self):
        """Test update method with *args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(1, 20, 30, 40, 50)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 40)
        self.assertEqual(r1.y, 50)

    def test_rectangle_update_kwargs(self):
        """Test update method with **kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=1, width=20, height=30, x=40, y=50)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 40)
        self.assertEqual(r1.y, 50)

    def test_rectangle_to_dictionary(self):
        """Test the dictionary representation of rectangle"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {'id': r1.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

if __name__ == '__main__':
    unittest.main()
