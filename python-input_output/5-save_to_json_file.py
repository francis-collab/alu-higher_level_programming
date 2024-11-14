#!/usr/bin/python3
"""
Module 5-save_to_json_file
Defines a function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.
    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
