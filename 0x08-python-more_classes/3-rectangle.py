#!/usr/bin/python3
"""This module contains a class 'Rectangle'"""


class Rectangle:
    """Thia class represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiates width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instance returns area of rectangle"""
        rect_area = self.__width * self.__height
        return rect_area

    def perimeter(self):
        """instance returns perimeter of rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            rect_prm = 2 * (self.__width + self.__height)
            return rect_prm

    def __str__(self):
        """returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for _ in range(self.__height):
            rectangle.append('#' * self.__width)
        return "\n".join(rectangle)

    def display(self):
        """prints the rectangle with "#" character"""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for _ in range(self.__height):
                print("#" * self.__width)
