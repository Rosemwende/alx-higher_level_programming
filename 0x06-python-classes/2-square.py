#!/usr/bin/python3
"""Define a square"""

class square:
    """square class with private instance attribute size"""
    def __init__(self, size=0):
        self.__size
    def size(self):
        """Getter method for size"""
        return self.__size
    def size(self, value):
        """setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
