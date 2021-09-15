#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for extern in matrix:
        row = []
        for intern in extern:
            row.append(intern**2)
        result.append(row)
    return result
