#!/usr/bin/python3
"""Module containing a function to write contents to a file"""


def write_file(filename="", text=""):
    """Write content to a file, whther it exists or not."""
    num_char = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        """open and overwrite content to a file"""
        num_char = f.write(text)
    return num_char
