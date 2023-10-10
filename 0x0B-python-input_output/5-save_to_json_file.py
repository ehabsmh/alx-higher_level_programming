#!/usr/bin/python3

"""
This module writes an Object to a text file,
using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):
    """
     writes an Object to a text file, using a JSON representation

    Args:
      my_obj: JSON representation of ``my_obj``
      filename: the file to write in the ``my_obj``.
    """

    with open(filename, "w") as wf:
        wf.write(json.dumps(my_obj))
