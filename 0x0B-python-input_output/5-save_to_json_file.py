#!/usr/bin/python3
""" Contains the save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON rep
    Args:
        1. my_obj: an object
        2. filename: name of file
    """
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
