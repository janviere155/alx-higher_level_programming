#!/usr/bin/python3
"""Module containing a function to translate the content
of an object into JSON format.
"""
import json


def to_json_string(my_obj):
    """JSON representation.
    Args:
        my_obj (str): the object to represent
    """
    json_str = json.dumps(my_obj)
    return json_str
