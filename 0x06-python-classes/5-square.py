#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """represent a square"""

    def __init__(self, size):
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

    def my_print(self):
        """print the square with #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
