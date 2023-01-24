#!/usr/bin/python3
"""Square Module"""

class Square:
    """Declares a square class"""

    def __init__(self, size = 0):
        """
        Initiaizes class attributes
        Args:
            size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than or equal to 0")
        else:
            self.__size = size

