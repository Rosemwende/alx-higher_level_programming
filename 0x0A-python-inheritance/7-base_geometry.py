#!/usr/bin/python3
"""Defines a class BaseGeometry with an integer validator method"""

class BaseGeometry:
    """A class with an integer validator method"""

    def area(self):
        """Raise an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
