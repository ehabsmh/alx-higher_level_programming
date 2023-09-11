#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a += (0, 0)
    tuple_b += (0, 0)

    t1 = tuple_a[0] + tuple_b[0]
    t2 = tuple_a[1] + tuple_b[1]

    return ((t1, t2))
