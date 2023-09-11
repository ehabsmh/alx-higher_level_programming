#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_n = min(my_list)
    for n in my_list:
        if n > max_n:
            max_n = n

    return max_n
