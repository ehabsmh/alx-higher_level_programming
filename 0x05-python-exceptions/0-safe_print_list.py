#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ prints x elements of a list. """
    i = 0

    while i < x:

        try:

            print(f"{my_list[i]}", end='')
            i += 1

        except IndexError:

            break

    print()

    return (i)
