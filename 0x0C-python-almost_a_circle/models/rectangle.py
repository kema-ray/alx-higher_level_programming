#!/usr/bin/python3
"""
Rectangle Class Module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Subclass
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of instances
        args:
            width: width of rectangle
            height: height of rectangle
            x: init variable
            y: init variable
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
