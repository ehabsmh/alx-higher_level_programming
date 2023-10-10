#!/usr/bin/python3

import json

"""
This module has a function that
returns the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
      my_obj: the object converted to JSON

    Return:
      the JSON representation of ``my_obj``
    """

    return json.dumps(my_obj)
