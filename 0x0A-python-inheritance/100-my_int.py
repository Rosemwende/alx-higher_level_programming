#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""

class MyInt(int):
    """A class representing an integer with inverted equality operators"""

    def __eq__(self, other):
        """Override equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality operator"""
        return super().__eq__(other)
