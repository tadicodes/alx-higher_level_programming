#!/usr/bin/python3
"""int validator"""


class BaseGeometry:
    """representation of BaseGeometry"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an int greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an int".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
