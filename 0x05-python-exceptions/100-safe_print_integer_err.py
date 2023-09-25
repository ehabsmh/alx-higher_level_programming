#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """
    prints an integer.
    Returns True if value has been correctly printed
    Otherwise, returns False
    and prints in stderr the error precede by Exception:
    """
    try:

        print("{:d}".format(value))
        return True

    except (ValueError, TypeError) as err:

        print(f"Exception: {err}", file=stderr)
        return False
