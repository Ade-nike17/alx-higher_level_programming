#!/usr/bin/python3
""""This module contains a class 'Rectangle'"""
from .base import Base


class Rectangle(Base):
    """This class 'Rectangle' inherits from 'Base'"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates:

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x coordinates, set to 0
            y: y coordinates, set ro 0
            id: id of the rectangle, set to None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """getter method for width"""
            return self.__width

        @width.setter
        def width(self, w):
            """setter method for width"""

            self.__width = w

        @property
        def height(self):
            """getter method for height"""
            return self.__height

        @height.setter
        def height(self, h):
            """setter method for height"""

            self.__height = h

        @property
        def x(self):
            """getter method for x"""
            return self.__x

        @x.setter
        def x(self, x):
            """setter method for x"""

            self.__x = x

        @property
        def y(self):
            """getter method for y"""
            return self.__y

        @y.setter
        def y(self, y):
            """setter method for y"""

            self.__y = y
