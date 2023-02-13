#!/usr/bin/python3
"""
Class Module
"""
import json


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

    def integer_validation(self, name, value):
        """
        check if value is an integer
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def integer_validation1(self, name, value):
        """
        check if value is an integer
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))


    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries or [])
