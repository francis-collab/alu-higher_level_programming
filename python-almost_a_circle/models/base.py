#!/usr/bin/python3
"""Base module."""
import json


class Base:
    """Base class for managing id attribute in future classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))
