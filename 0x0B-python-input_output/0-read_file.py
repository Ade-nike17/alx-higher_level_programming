#!/usr/bin/python3
""" Contains the read_file function """


def read_file(filename=""):
    """ reads a textfile and prints to the stdout """
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read())
