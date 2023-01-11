#!/usr/bin/python3
"""MOdule containing function to append content to a file."""


def append_write(filename="", text=""):
    """Append new content, without overwriting existing one."""
    num_char = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        """use the ``a`` mode to append content"""
        num_char = f.write(text)
    return num_char
