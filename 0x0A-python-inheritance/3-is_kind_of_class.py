#!/usr/bin/python3
"""Definition of ``is_kind_of_class`` function."""


def is_kind_of_class(obj, a_class):
    """Determine if obj is an instance of a_class.

    Args:
        obj (object): object
        a_class (str): class

    Returns:
        True: if it is
        False: if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
