#!/usr/bin/python3

"""
This module defines a student
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # _________________________________________________________________

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of Student instance"""

        is_str = False
        attrs_dict = {}

        if type(attrs) is list:
            is_str = all([type(att) is str for att in attrs])

            if is_str:
                for att in attrs:
                    if att not in self.__dict__:
                        continue

                    attrs_dict[att] = self.__dict__[att]

                return attrs_dict

        return self.__dict__

    # _________________________________________________________________

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
          json: will always be a dictionary
        """
        self.__dict__ = json
