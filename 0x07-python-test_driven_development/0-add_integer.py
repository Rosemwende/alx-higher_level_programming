#!/usr/bin/python3

"""Module for adding two integers"""

def add_integer(a, b=98):
    """adds two integers
    
    Args:
    a (int): The first integer
    b (int, optional): The second integer Defaults to 98

    Returns the addition of a and b
    Raises:
    TypeError: if a or b is not an integer or float"""
    if not isinstance(a, (int, float)):
        raise(TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise(TypeError("b must be an integer")
    return int(a) + int(b)
