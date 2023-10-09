#!/usr/bin/python3

"""
This module defining one function,
returns True if the object is exactly an instance
of the specified class otherwise False.
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly an instance
    of the specified class otherwise False.

    Args:
      obj: The object to check of
      a_class: The class to check the object with

    Return:
      True: if the object is exactly an instance of the specified class
      False: if the object is not an instance of the class
    """

    return (isinstance(obj, a_class))
