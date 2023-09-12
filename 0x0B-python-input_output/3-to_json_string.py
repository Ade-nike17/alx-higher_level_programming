#!/usr/bin/python3
""" Contains the to_json_string function """
import json


def to_json_string(my_obj):
    """returns the JSON rep of a string
    Args:
        1. my_obj: an object
    """
    return json.dumps(my_obj)
