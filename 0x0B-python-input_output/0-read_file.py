#!/usr/bin/python3
"""Module containing a function to read contents of a file"""


def read_file(filename=""):
    """Read the contents of a file."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
