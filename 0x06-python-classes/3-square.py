#!/usr/bin/python3
"""Square Module"""

class Square:
    """
    Declares a square class
    """
    def __init__(self, size = 0):
        """
        Initializes class attributes
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of a square
        """
        return self.__size ** 2
