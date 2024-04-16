#!/usr/bin/python3
"""Defines a Student class with public instance attributes and a method to convert it to JSON"""

class Student:
    """Defines a student by first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with given attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
