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

    def __str__(self):
        """String representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Compute the area of the rectangle"""
        return self.__width * self.__height
