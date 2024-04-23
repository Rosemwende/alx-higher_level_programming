#!/usr/bin/python3
""" Rectangle class module """

from models.base import Base

class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints the Rectangle instance with # """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
