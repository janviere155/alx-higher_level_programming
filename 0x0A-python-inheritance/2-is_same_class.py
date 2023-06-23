#!/usr/bin/python3
"""Module containing function ``is_same_class``"""


def is_same_class(obj, a_class):
    """Are they of the same class
    Args:
        obj (any type): object to check
        a_class (str): the class to check
    Returns:
        True: if of same class
        False: not of the same class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
