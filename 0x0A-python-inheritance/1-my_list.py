#!/usr/bin/python3

"""
This module contains a class that inherits
from other class

The class `MyList` contains only one function
that prints sorted list in ascending order.
"""


class MyList(list):
    """
    This class inherits from list class
    contains only one function that prints the list
    """

    def print_sorted(self):
        """
        This function prints the list,
        but sorted in ascending order.
        """

        sorted_list = sorted(self)
        print(sorted_list)
