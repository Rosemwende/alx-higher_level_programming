#!/usr/bin/python3
#0-add_integer.py
"""Module for adding two integers"""

def add_integer(a, b=98):
    """Adds two integers
    
    Args:
    a (int): The first integer
    b (int, optional): The second integer. Defaults to 98

    Returns the integer addition of a and b"""
    if ((not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
