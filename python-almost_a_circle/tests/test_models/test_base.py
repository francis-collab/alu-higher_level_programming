#!/usr/bin/python3
"""Test cases for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """Test the functionality of the Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatic ID assignment"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test custom ID assignment"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_to_json_string(self):
        """Test conversion of list of dictionaries to JSON string"""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, '[{"id": 1}, {"id": 2}]')

        json_str_empty = Base.to_json_string(None)
        self.assertEqual(json_str_empty, '[]')

    def test_save_to_file(self):
        """Test saving list of objects to a file in JSON format"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_from_json_string(self):
        """Test conversion of JSON string to list of dictionaries"""
        json_str = '[{"id": 1}, {"id": 2}]'
        list_dicts = Base.from_json_string(json_str)
        self.assertEqual(list_dicts, [{"id": 1}, {"id": 2}])

        list_dicts_empty = Base.from_json_string("")
        self.assertEqual(list_dicts_empty, [])

    def test_create(self):
        """Test creation of an instance from dictionary"""
        dict = {"id": 1, "width": 1, "height": 1, "x": 0, "y": 0}
        r = Rectangle.create(**dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_load_from_file(self):
        """Test loading list of instances from a file"""
        Rectangle.save_to_file(None)
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])

if __name__ == '__main__':
    unittest.main()
