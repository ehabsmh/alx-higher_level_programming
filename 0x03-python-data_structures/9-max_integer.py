#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_n = 0
    for elem in my_list:
        if elem > max_n:
            max_n = elem
    return max_n
