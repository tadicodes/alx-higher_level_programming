#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely

    Args:
        fct: function to execute
        args: Arguments for fct

    Returns:
        If error occurs - None
        else - the result of the call to fct
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
