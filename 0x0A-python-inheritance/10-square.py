#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""

class BaseGeometry:
    """A class with an area method and integer validator method"""

    def area(self):
        """Raise an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initialize a rectangle with specified width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """A class representing a square"""

    def __init__(self, size):
        """Initialize a square with specified size"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
