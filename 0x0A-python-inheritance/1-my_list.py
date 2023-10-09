#!/usr/bin/python3

"""
This module contains class MyList that inherits from list
"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
