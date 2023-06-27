#!/usr/bin/python3
"""define a magic class matching exactly a bytecode provided by ALX"""

import math


class MagicClass:
    """represent circle"""

    def __init__(self, radius=0):
        """initialize a magic class

        Arg:
            radius (float or int): radius of the new magic class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the area of the Magic class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference of Magic class"""
        return (2 * math.pi * self.__radius)
