#!/usr/bin/python3
""" This is a matrix divide module """


def matrix_divided(matrix, div):
    """
    Divide all elements in a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided by `div`.

    Raises:
        TypeError: If the `matrix` is not a matrix (list of lists) of integers/floats,
            or if the rows in the matrix have different sizes.
        TypeError: If the `div` is not a number.
        ZeroDivisionError: If `div` is zero.
    """
    if not isinstance(matrix, list) or not matrix or any(not isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(matrix, list) or not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    row_size = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != row_size:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    result = [[round(num / div, 2) for num in row] for row in matrix]
    return result
