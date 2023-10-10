#!/usr/bin/python3

"""
This module converts a JSON string to an object (py DS)
"""


import json


def from_json_string(my_str):
    """
     returns an object (Python data structure) represented by a JSON string:

    Args:
      my_str: the string converted to object (Data structure)

    Return:
      the object of ``my_str``.
    """

    return json.loads(my_str)
