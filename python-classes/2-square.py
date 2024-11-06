#!/usr/bin/python3
"""Module 2-square
Defines a Square class with size attribute and validation.
"""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a size attribute.
        
        Args:
            size (int): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
