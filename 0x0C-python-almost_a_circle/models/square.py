#!/usr/bin/python3
""" Square class module """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns string representation of the instance """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

        def update(self, *args, **kwargs):
        """ Assigns arguments to attributes """
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
