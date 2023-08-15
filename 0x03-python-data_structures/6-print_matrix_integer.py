#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx, value in enumerate(row):
            print("{:d}".format(value), end="")
            if col_idx < len(row) - 1:
                print(" ", end="")

        print()
