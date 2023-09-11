#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    list_len = len(my_list)
    
    list_cpy = my_list.copy()

    if ((idx < 0) or (idx > list_len - 1)):
        return (list_cpy)

    list_cpy[idx] = element

    return (list_cpy)
