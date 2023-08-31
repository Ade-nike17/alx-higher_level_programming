#!/usr/bin/python3
"""This module contains a class 'Square'"""


class Square:
    """This class represents a Square"""
    def __init__(self, size=0):
        """ Instantiatiating size"""
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
        """A public instance method 'area'"""
        curr_sq_area = self.__size * self.__size
        return curr_sq_area

    def my_print(self):
        """Prints the square using the '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
