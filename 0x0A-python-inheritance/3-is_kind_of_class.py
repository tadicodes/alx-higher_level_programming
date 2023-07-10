#!/usr/bin/python3
"""same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """checks if object is instance of, or if the object is an instance
    of a class that inherited from, the specified class"""

    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
