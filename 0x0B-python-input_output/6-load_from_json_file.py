#!/usr/bin/python3
"""Module to load content from a JSON file"""
import json


def load_from_json_file(filename):
    """use the load() method"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
