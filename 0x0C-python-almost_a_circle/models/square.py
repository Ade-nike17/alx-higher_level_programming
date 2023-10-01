#!/usr/bin/python3
"""
The `rectangle` module.
This module defines a Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates

        Args:
            size: The size of the square
            x: x coordinate. Defaults to 0.
            y: y coordinate. Defaults to 0.
            id: id of the square. Defaults to None.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the 'Square'"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
