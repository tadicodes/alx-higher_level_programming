#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format()

    Args:
        value (int): integer to print

    Returns:
        TypeError or ValueError - False
        Else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
