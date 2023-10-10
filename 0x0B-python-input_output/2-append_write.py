#!/usr/bin/python3

"""This module appends a string at a file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added

    Args:
      filename: The file to append on it
      text: The text will be appended to the file

    Return:
      The number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as af:
        af.write(text)

    return len(text)
