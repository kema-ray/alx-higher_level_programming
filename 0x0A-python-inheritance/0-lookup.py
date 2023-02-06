#!/usr/bin/python3
"""
The lookup function
"""


def lookup(obj):
    """
    Args:
        obj: initial object
        Returns: a list of available attributes
                 and objects of an object
    """

    return dir(obj)
