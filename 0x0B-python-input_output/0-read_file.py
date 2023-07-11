#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """""reads text file (UTF8) and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
