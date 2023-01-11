#!/usr/bin/python3
"""Module to contain the function to load content
from a JSON file.
"""
import json


def from_json_string(my_str):
    """Return the string in th eJSON file."""
    new = json.loads(my_str)
    return new
