#!/usr/bin/python3
""" Contains the append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file
    Args:
        1. filename: name of file
        2. search_string: the string to search
        3. new_string: the string to append
    """
    text = ""
    with open(filename) as fo:
        for line in fo:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w") as f:
        f.write(text)
