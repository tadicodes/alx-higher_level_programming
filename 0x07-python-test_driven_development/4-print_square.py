#!/usr/bin/python3
# 4-print_square.py
"""defines a square-printing function"""


def print_square(size):
    """print a square with the # character

    Args:
        size (int): The height/width of square
    Raises:
        TypeError: if size is not an int
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an int")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
