#!/usr/bin/python3
"""
Module that defines a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Definition of class MyInt that inherits from class int
    """
    def __eq__(self, value):
        """
        overrides equals, inverting it
        """
        return int(self) != int(value)

    def __ne__(self, value):
        """
        overrides not-equals, inverting it
        """
        return int(self) ==  int(value)
