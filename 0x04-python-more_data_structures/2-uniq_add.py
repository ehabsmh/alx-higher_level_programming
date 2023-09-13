#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    total_sum = 0

    for n in my_set:
        total_sum += n

    return total_sum
