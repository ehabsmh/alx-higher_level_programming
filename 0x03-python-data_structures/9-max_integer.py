#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_val = 0
    for n in my_list:
        if (n > max_val):
            max_val = n

    return max_val
