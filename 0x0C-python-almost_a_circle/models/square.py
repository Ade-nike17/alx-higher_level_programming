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

    @property
    def size(self):
        """getter method for square"""
        return self.height

    @size.setter
    def size(self, value):
        """setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns arguments to attributes in the specified order"""
        num_args = len(args)
        if (num_args >= 1):
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        else:
            if kwargs.get('size'):
                self.size = kwargs['size']
            super().update(*args, **kwargs)
