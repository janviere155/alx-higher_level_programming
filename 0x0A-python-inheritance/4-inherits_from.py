#!/usr/bin/python3
"""Module containing the ``inherits_from`` function."""


def inherits_from(obj, a_class):
    """Check whether it inherits from a class.

    Args:
        obj: the object to test
        a_class: the class to check

    Returns:
        True: if it is
        False: if not
    """
    if issubclass(type(obj), a_class) and (type(obj) != a_class):
        return True
    else:
        return False
