#!/usr/bin/python3
"""
Class Module
"""


class Base:
    """
    Base Class
    Attributes:
        __nb_objects: number of objects created
        id: id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization method
        args:
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
