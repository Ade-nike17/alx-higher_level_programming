#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """
import sys
import json
from os.path import exists


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
