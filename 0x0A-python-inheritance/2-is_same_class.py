#!/usr/bin/python3
"""
Function that returns a True if its exact same object
"""


def is_same_class(obj, a_class):
    """
    Check if the object is  exactly an instance of the specified class
    Args:
        obj: initial object
        a_class: class to confirm with the object
    Returns: True if object is an exactly the instance of the class
             or False if not
    """

    if type(obj) is not a_class:
        return False
    else:
        return True
