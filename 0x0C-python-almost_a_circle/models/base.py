#!/usr/bin/python3
"""
The Base module
This class will be the “base” of all other classes in this project
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        elif not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
