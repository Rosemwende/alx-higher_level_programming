#!/usr/bin/python3

"""Defines a Square"""

class Square:
    """Square with private instance attribute size"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """method to calculate the area of a square"""
        return self.__size ** 2
