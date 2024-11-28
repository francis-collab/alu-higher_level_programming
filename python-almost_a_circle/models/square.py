#!/usr/bin/python3
"""Square module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, affecting width and height."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
