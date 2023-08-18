#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    squared_matrix = []
    for row in matrix:
        squared_row = [n * n for n in row]
        squared_matrix.append(squared_row)
    return squared_matrix
