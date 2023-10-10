#!/usr/bin/python3

"""
This module creates an Object from a "JSON file":
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"

    Args:
      filename: the file to create the object from.
    """

    with open(filename, "r") as rf:
        data = json.loads(rf.read())

    return data
