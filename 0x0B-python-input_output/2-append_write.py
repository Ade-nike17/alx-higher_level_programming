#!/usr/bin/python3
""" contains the append_write function """


def append_write(filename="", text=""):
    """appends string.
    Args:
        1. filename: name of file to be appended.
        2. text: strings to append to the file.
    Return: number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        nbChars = f.write(text)
    return nbChars
