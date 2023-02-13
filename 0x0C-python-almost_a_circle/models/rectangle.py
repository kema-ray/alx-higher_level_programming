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

    @property
    def width(self):
        """
        getter method for width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        setter method for width
        """
        self.integer_validation('width', value)
        self.__width = value

    @property
    def height(self):
        """
        getter method for height
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        setter method for width
        """
        self.integer_validation('height', value)
        self.__height = value

    @property
    def x(self):
        """
        getter method for x
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        setter method for x
        """
        self.integer_validation1('x', value)
        self.__x = value

    @property
    def y(self):
        """
        getter method for y
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        setter method for y
        """
        self.integer_validation1('y', value)
        self.__y = value

    def area(self):
        """
        returns the area of the rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
        prints  in stdout the Rectangle instance 
        with the character #
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

        def __str__(self):
            """
            returns a string format of the rectangle
            """
            return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)
