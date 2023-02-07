#!/usr/bin/python3
"""
Module for class Student
"""


class Student:
    """
    Student representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Student initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        retrieves a dictionary representation of a Student instance
         Args:
              attr (list): attribute names that are to be retrieved.
        """
        if attr is not None:
            result = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return result
        else:
            return self.__dict__
