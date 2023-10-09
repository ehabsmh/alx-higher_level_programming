#!/usr/bin/python3

"""
This module contains one function,
that returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class, otherwise False.
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class otherwise False

    Args:
      obj: The object to check of
      a_class: The class to check the object with

    Return:
      True: if the object is an instance of a class
            that inherited (directly or indirectly)
            from the specified class
      False: if the object is not an instance of the class.
    """

    if not issubclass(a_class, obj.__class__):
        return True
    else:
        return False
