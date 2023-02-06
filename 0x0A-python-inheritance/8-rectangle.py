#!/usr/bin/python3
"""
Module that contains the class BaseGeometry  and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle representation"""
    def __init__(self, width, height):
        """
        Initializing function
        Args:
            width: variable to be initialized
            height: variable to be initialized
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
