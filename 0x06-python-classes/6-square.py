#!/usr/bin/python3
"""Defines a Square"""

class Square:
    """Square class with private instance attributes size and position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    def size(self):
        """Getter method for size"""
        return self.__size

    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def position(self):
        """Getter method for position"""
        return self.__position

    def position(self, value):
        """Setter method for position"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
