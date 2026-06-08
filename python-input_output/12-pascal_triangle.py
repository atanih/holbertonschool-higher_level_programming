#!/usr/bin/python3
"""Module that returns a list of lists
representing Pascal's triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers
    representing Pascal's triangle of n.

    Args:
        n: The number of rows of Pascal's triangle to generate

    Returns:
        A list of lists of integers, or empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
