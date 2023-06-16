#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if len(matrix) == 0:
        return 0
    new = map(lambda x: list(map(lambda y: y**2, x)), matrix)
    return list(new)
