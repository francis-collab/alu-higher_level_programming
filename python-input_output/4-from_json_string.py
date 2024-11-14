#!/usr/bin/python3
"""
Module 4-from_json_string
Defines a function that returns an object
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    Args:
        my_str (str): The JSON string to convert.
    Returns:
        object: The Python data structure
    """
    return json.loads(my_str)
