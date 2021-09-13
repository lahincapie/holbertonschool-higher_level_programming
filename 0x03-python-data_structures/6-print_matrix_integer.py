#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for column in matrix:
        for row in column:
            print('{:d}'.format(row), end='')
            if row != (column[len(column) - 1]):
                print('', end=' ')
        print('')
