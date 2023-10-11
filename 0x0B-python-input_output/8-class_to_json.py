#!/usr/bin/python3

"""
returns the dictionary description
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure 
    for JSON serialization of an object

    Args: an instance of a Class
    """
    new_obj = obj.__dict__
    return new_obj
