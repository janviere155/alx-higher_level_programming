#!/usr/bin/python3
"""Class ``Rectangle`` inherits the ``BaseGeometry`` class."""


base_g = __import__('7-base_geometry')


class Rectangle(base_g.BaseGeometry):
    """Class Definition"""

    def __init__(self, width, height):
        """Initialize the attributes"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
