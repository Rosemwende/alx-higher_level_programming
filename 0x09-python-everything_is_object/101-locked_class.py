#!/usr/bin/python3
"""Defines a locked Class"""

class LockedClass:
    """Prevents the user from dynamically creating new
    new instance attributes except if the new instance
    attribute is called 'first_name'"""

    __slots__ = ["first_name"]
