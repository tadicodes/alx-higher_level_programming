#!/usr/bin/python3
"""only sub class of"""


def inherits_from(obj, a_class):
    """checks if object is an instance of a class that inherited
    (directly or indirectly) from the specified class"""

    return (type(obj) is not a_class and issubclass(type(obj), a_class))
