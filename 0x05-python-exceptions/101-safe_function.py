#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """
    function that executes a function safely.
    Returns the result of the function, Otherwise,
    returns None if something happens during the function
    and prints in stderr the error precede by "Exception:"
    """
    try:

        return fct(*args)

    except Exception as err:

        print(f"Exception: {err}", file=stderr)
        return None
