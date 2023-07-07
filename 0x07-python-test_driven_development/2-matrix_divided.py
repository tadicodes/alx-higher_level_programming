#!/usr/bin/python3
# 2-matrix_divided.py
"""defines a matrix division function"""


def matrix_divided(matrix, div):
    """divide all elements of a matrix

    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float): The divisor
    Raises:
        TypeError: if matrix contains non-numbers
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0
    Returns:
        new matrix representing result of division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "ints/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("each row of matrix must have same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a no.")

    if div == 0:
        raise ZeroDivisionError("divide by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
