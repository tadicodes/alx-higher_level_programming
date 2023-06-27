#!/usr/bin/python3
"""define a class square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initialize a new square

        Args:
            size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """set the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current area of square"""
        return (self.__size * self.__size)
