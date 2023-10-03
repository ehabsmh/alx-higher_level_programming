#!/usr/bin/python3

"""
This is the "4-print_square" module

The "4-print_square" module contains one function, print_square()
"""


def print_square(size):
    """prints a square with the character #
    Args:
      size (int): The size of the square.

    Raises:
      TypeError: If `size` isn't integer.
      ValueError: If `size` is less than 0.
    """

    """ Check: size must be an integer """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    """ Check: size is less than 0 """
    if size < 0:
        raise ValueError("size must be >= 0")

    """ Print: The squares """
    for _ in range(size):

        for _ in range(size):

            print('#', end='')

        print()
