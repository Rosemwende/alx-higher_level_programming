#!/usr/bin/python3
"""defines a function to lookup attributrs andmethods of an object"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
