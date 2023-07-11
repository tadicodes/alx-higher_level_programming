#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """writes string to a text file (UTF8)
    and returns number of chars written"""
    with open(filename, 'w', encoding='utf=8') as file:
        return file.write(text)
