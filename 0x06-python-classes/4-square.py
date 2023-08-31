#!/usr/bin/python3
"""This module contains a class 'Square'"""


class Square:
    """This class representa a 'Square'"""
    def __init__(self, size=0):
        """Instatiates size"""
        self.size = size

    @property
    def size(self):
        """Getter method for 'size'"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for 'size'"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area"""
        curr_sq_area = self.__size * self.__size
        return curr_sq_area
