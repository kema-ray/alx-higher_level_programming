#!/usr/bin/python3
"""
The is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of a specified class
    Args:
        obj: initial object
        a_class: class to confirm the object
    Returns: True if object is an instance of or inherited the class
             or False if not
    """
    return (isinstance(obj, a_class))
