#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for n in range(row_len):
            print("{}".format(row[n]), end=' ' if n < row_len - 1 else '')

        print()
