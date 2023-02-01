#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Args:
        matrix: initial 2D list
        div: integer with the divisor
    Returns:
        New matrix containing the divided elements rounded to 2 decimal places
    """

    previous_len = 0
    error_message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_message)

    for block in matrix:    # matrix is a list
        if type(block) is not list:
            raise TypeError(error_message)

        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_message)

        if len(block) != previous_len and previous_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        previous_len = len(block)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
