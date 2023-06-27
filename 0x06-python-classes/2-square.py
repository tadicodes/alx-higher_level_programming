#!/usr/bin/python3
"""define class square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initialize new square

        Args:
            size (int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
