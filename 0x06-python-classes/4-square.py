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
        self.size = size

    @property
    def size(self):
        """
        Gets the attributes to be used in the class
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of a square
        """
        return self.__size ** 2
