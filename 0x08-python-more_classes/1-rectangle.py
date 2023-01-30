#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, height=0, width=0):
        """ Method that intializes the instance
        Args:
            height: rectangle height
            width: rectangle width
        """
        self.height = height
        self.width = width


    @property
    def height(self):
        """
        method that returns the value of the height
        Returns:
            rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=  0")
        self.__height = value

    @property
    def width(self):
        """
        method that returns the value of the width
        Returns:
            rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Method that defines the width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=  0")
        self.__width = value

