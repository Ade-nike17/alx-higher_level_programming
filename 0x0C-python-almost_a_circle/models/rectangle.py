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
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Instance returns area of Rectangle"""
        rect_area = self.__width * self.__height
        return rect_area

    def display(self):
        """prints rectangle with '#' character"""
        for _ in range(self.y):
            print()

        for _ in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """returns a string representation of the 'Rectangle'"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"
