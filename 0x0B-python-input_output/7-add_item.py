#!/usr/bin/python3
"""
This script adds command line arguments to a Python list and saves them to a file.

Usage:
        ./script_name.py arg1 arg2 ...

        The script uses the 'save_to_json_file' and 'load_from_json_file' functions to save and load the list from a JSON file.
"""

import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

# check if add_item.jsonfile exists
try:
    # load the existing lists from the file
    my_list = load_from_json_file("add_item.json")

except FileNotFoundError:
    # create a new list if file does not exist
    my_list = []

# add command line argument to the list
my_list.extend(sys.argv[1:])

# save the updated list to add_item.json
save_to_json_file(my_list, "add_item.json")
