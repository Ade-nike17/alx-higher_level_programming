#!/usr/bin/python3
"""This module contains a class 'Rectangle'"""


class Rectangle:
    """This class represents a 'Rectangle'"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiating width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """returns area of the rectangle"""
        rect_area = self.__width * self.__height
        return rect_area

    def perimeter(self):
        """returns perimeter of the rectangle"""
        rect_prm = 2 * (self.__width * self.__height)
        return rect_prm

    def __str__(self):
        """returns string representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += (str(self.print_symbol) * self.__width) + "\n"
        return result.rstrip("\n")

    def __repr__(self):
        """returns a string representation of Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
