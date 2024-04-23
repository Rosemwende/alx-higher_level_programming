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

    def __str__(self):
        """ Returns string representation of the instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """ Prints the Rectangle instance with # """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """ Assigns arguments to attributes """
        attr_names = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attr_names[i], args[i])

    def update(self, *args, **kwargs):
        """ Assigns arguments to attributes """
        if args:
            attr_names = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
