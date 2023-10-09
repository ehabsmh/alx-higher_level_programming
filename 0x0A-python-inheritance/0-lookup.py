#!/usr/bin/python3

"""
This module contains a lookup function
that returns the list of available attributes and methods of an object.

"""


def lookup(obj):
    """
    This function returns the list of available attributes and methods obj

    Args:
      obj: The object to look for available attributes and methods

    Return:
      a list object contains available attributes and methods.
    """

    return dir(obj)
