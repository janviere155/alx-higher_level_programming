#!/usr/bin/python3
"""Module contains functon to save to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Save JSON content to a file."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
