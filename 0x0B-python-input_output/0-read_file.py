#!/usr/bin/python3

"""This module contains one function"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
      filename: The filename to read from.
    """
    with open(filename) as rf:
        print(rf.read(), end='')
