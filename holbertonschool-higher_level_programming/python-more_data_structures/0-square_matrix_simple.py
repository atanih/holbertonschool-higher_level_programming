#!/usr/bin/python3
"""Module that defines square_matrix_simple."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.

    Args:
        matrix (list of lists of int): the 2D input matrix.

    Returns:
        list of lists of int: a new matrix with each value squared.
        The original matrix is not modified.
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
