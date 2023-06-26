#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an int with "{:d}".format()

    If ValueError message is caught, a corresponding
    message is printed to standard error

    Args:
        value (int): int to print

    Returns:
        TypeError or ValueError - False
        Else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
