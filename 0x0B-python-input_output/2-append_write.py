#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """appends string at the end of a text file (UTF8)
    and returns number of chars added"""
    with open(filename, 'a', encoding='utf=8') as file:
        return file.write(text)
