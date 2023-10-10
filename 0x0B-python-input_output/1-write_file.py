#!/usr/bin/python3

"""
This module writes in files
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
      filename: The file to write in it
      text: The text will be written to the file.
    """
    n_chars = 0

    with open(filename, "w") as wf:
        n_chars = wf.write(text)

    return (n_chars)
