#!/usr/bin/python3
# 5-text_indentation.py
"""defines a text-indentation function"""


def text_indentation(text):
    """print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): text to print
    Raises:
        TypeError: text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
