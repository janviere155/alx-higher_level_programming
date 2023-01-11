#!/usr/bin/python3
"""Module designed to contain the ``Student`` class"""


class Student:
    """Class definition of Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the arguments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve the dictionary representation of a class"""
        return self.__dict__
