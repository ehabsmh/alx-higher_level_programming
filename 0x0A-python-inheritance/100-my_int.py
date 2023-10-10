#!/usr/bin/python3

"""This module contains one class"""


class MyInt(int):
    """define MyInt"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
