#!/usr/bin/python3
"""Module to modify the base_geometry class"""


class BaseGeometry:
    """BaseGeometry class definition"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if ``value`` is an integer.
        Args:
            name (str): parameter name
            value (int): integer value
        Raises:
            TypeError: if not an integer
            ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
