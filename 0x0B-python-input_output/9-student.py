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

    def to_json(self):
        """retrieves a dictionary representation of Student instance"""
        return self.__dict__
