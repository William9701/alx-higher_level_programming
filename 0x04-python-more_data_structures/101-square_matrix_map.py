#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if len(matrix) != 0:
        return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
    return 0
