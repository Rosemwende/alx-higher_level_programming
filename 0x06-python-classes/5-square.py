#!/usr/bin/python3
"""Defines a Square"""

class Square:
    """Square class with private instance attribute size"""
    def __init__(self, size=0):
        self.__size = size

    def size(self)
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

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
