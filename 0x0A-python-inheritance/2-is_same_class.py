#!/usr/bin/python3
"""exact same object"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of given class"""

    return (type(obj) is a_class)
