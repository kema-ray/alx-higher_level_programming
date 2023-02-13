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

    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        args:
            list_objs: list of objects
        """
        if list_objs:
            i = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            i = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(i)

    def from_json_string(json_string):
        """
        json to string static method
        args:
            json_string: json object string type
        return:
            list of json strings
        """
        if json_string:
            return json.loads(json_string)
        return []

    def create(cls, **dictionary):
        """
        return instance with all attributes already set
        args:
            dictionary: double pointer
        return:
            instance with set attribute
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    def load_from_file(cls):
        """
        returns a list of instances
        """
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                d = cls.from_json_string(f.read())
            return [cls.create(**i) for i in d]
        except FileNotFoundError:
            return []
