#!/usr/bin/python3
""" Square module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
