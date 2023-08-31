#!/usr/bin/python3
"""Thic module contains a class 'MagicClass'"""


import math


class MagicClass:
    """This class represents 'MagicClass'"""
    def __init__(self, radius=0):
        """Instantiating 'radius'"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """A public instance method 'area'"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """A public instance method 'circumference'"""
        return 2 * math.pi * self.__radius
