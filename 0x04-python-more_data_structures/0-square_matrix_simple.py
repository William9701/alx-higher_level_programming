#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        new_m = []
        for i in matrix:
            new_row = []
            for elem in i:
                new_elem = elem ** 2
                new_row.append(new_elem)
            new_m.append(new_row)
        return new_m
