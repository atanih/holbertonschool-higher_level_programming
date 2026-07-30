#!/usr/bin/python3
"""Module 2-matrix_divided.

Defines a single function ``matrix_divided`` that divides all the
elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    The matrix must be a list of lists of integers or floats and all
    the rows must have the same size. Returns a new matrix with each
    element rounded to 2 decimal places.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(err)
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError(err)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
