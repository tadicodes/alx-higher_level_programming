#!/usr/bin/python3
"""define class square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initialize a new square

        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the current area of square"""
        return (self.__size * self.__size)
