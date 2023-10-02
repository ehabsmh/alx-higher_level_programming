#!/usr/bin/python3

"""prints My name is <first name> <last name>
Args:
  first_name: as the name suggest
  last_name: as the name suggest
"""


def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    message = "My name is {:s} {:s}"
    print(message.format(first_name, last_name))
