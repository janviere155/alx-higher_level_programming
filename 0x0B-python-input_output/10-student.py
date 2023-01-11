#!/usr/bin/python3
"""Module designed to contain the ``Student`` class"""


class Student:
    """Class definition of Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the arguments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve the dictionary representation of a class"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = dict()
            old_dict = self.__dict__
            for (key, value) in old_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
