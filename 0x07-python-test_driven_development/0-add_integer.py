#!/usr/bin/python3
# 0-add_integer.py
"""defines an int addition function"""


def add_integer(a, b=98):
    """return the int addition of a and b

    float arguments are typecasted to ints before addition is performed

    raises:
        TypeError: If either of a or b is a non-int and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an int")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an int")
    return (int(a) + int(b))
