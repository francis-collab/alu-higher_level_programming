#!/usr/bin/python3
"""Module 4-square
Defines a Square class with size attribute, validation, and methods to access
and update the size.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a size attribute.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
