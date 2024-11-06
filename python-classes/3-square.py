#!/usr/bin/python3
"""Module 3-square
Defines a Square class with size attribute, validation and area calculation.
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

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
