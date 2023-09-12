#!/usr/bin/python3
"""contains the write_file function """


def write_file(filename="", text=""):
    """writes string.
    Args:
        1. filename: name of the file to be written.
        2. text: strings to write in file.

    Return: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        nbChars = f.write(text)
    return nbChars
