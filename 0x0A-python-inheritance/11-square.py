#!/usr/bin/python3
"""Module containing ``Square`` class inheriting from
``Rectangle`` class
"""


base_g = __import__('9-rectangle')


class Square(base_g.Rectangle):
    """Class definition"""
    def __init__(self, size):
        """Initialize the square attributes"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """String representation"""
        return f"[Square] {self.__size}/{self.__size}"
