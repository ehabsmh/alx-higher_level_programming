#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix. """
    new_matrix = matrix.copy()

    for i, row in enumerate(matrix):
        new_matrix[i] = list(map(lambda n: n ** 2, row))

    return new_matrix
