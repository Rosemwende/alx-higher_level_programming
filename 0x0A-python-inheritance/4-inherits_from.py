#!/usr/bin/python3

"""Defines a function to check if an object inherits from a specified class"""

def inherits_from(obj, a_class):
    """Check if an object inherits from a specified class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
