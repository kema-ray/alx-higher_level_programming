#!/usr/bin/python3
"""
Module for load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as file:
        create_object = json.load(file)
        return create_object
