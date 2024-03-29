#!/usr/bin/python3
"""
Contains function that returns a number lines in text file
"""


def write_file(filename="", text=""):
    """
    Return number of lines in text file
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
