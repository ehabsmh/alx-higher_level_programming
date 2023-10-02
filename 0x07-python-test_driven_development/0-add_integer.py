#!/usr/bin/python3

"""Addition Module
    Args:
        a: first argument; type must be int or float.
        b: second argument; default is 98. If given must be int or float
"""


def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
