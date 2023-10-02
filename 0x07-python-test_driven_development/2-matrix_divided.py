#!/usr/bin/python3

"""divide matrix module
Args:
  matrix: list of lists
  div: The divisor
"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix. """

    """ matrix must be a list of lists """
    if (not isinstance(matrix[0], list) or
            not isinstance(matrix, list)):

        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    """ div must be a number (integer or float) """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """ div can't be equal to 0 """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_len = len(matrix)

    for i in range(matrix_len):

        for j in range(i + 1, matrix_len):

            """ matrix must be a list of lists of integers or floats """
            if not isinstance(matrix[i][j - 1], (int, float)):

                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

            """ Each row of the matrix must be of the same size """
            if len(matrix[i]) != len(matrix[j]):

                raise TypeError(
                    "Each row of the matrix must have the same size")

    """ divide by div, rounded to 2 decimal places """
    new_matrix = [[round(n / div, 2) for n in row] for row in matrix]

    return new_matrix
