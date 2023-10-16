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

    # ___________________________________________________________________

    @classmethod
    def save_to_file(cls, list_objs):

        list_instances = []

        if list_objs:
            for ob in list_objs:
                list_instances.append(ob.to_dictionary())

        list_instances = cls.to_json_string(list_instances)

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as wf:

            wf.write(list_instances)

    # ___________________________________________________________________

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
