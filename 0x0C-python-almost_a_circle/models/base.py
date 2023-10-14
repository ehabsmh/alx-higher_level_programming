#!/usr/bin/python3

"""
This module manages id attribute in subclasses
"""


class Base:
    """Defines objects of type Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes Base objects

        Args:
            self: refers to any object created of type Base
            id: identifier for any object created
         """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
