#!/usr/bin/python3

"""
This module contains only one function,
"""


def inherits_from(obj, a_class):
    """function that returns Truesi the object is an instance of a class
     that inherited (directly or indirectly) from the specified class"""

    if not issubclass(a_class, obj.__class__):
        return True

    return False
