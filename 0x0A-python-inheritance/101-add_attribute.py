#!/usr/bin/python3
"""Defines a function to add a new attribute to an object if possible"""

def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible"""
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and attr in obj.__slots__):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
