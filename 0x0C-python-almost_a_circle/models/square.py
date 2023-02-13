#!/usr/bin/python3
"""
Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization method
        Args:
            size: size of square
            x: x position
            y: y position
            id: object id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns a string format of the square
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.height))

    @property
    def size(self):
        """
        width getter method
        return:
            size of width and height
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        width and height setter method
        args:
            value: size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update square method
        args:
            args: pointer to arguments
            kwargs: double pointer to key word arguments
        """
        if args:
            i = 0
            list = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, list[i], arg)
                i += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """
        returns a dictionary representation of the square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 
                'y': self.y}
