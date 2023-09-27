#!/usr/bin/python3
"""
The Base module
This class will be the “base” of all other classes in this project
"""


class Base:
    """This class represents the Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiates id"""
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
