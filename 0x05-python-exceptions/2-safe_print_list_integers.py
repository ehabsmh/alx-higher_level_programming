#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ Prints the first x elements of a list and only integers. """
    i = 0

    printed_integers = 0
    while (i < x):
        try:

            print("{:d}".format(my_list[i]), end='')
            printed_integers += 1
            i += 1

        except (TypeError, ValueError):
            i += 1
            continue

        except IndexError:
            raise

    print()

    return (printed_integers)
