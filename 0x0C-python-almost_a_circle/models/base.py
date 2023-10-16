#!/usr/bin/python3

"""
This module manages id attribute in subclasses
"""

import json


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

    # ___________________________________________________________________

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: a list of dictionaries

        Return: "[]" if list_dictionaries is None or empty OTHERWISE,
                return the JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
