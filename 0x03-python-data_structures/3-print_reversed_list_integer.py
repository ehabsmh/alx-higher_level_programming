#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    sorted_list = sorted(my_list)
    sorted_list.sort(reverse=True)

    for n in sorted_list:
        print("{:d}".format(n))
