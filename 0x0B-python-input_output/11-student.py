#!/usr/bin/python3
"""Defines a Student class with public instance attributes and methods to convert it to JSON,
save it to a file, and reload from JSON file"""

import json

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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with the values from the given JSON"""
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
    import os
    import sys

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

    with open(path, 'w') as file:
        json.dump(j_student_1, file)

    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    print("Load dictionary from file:")
    with open(path, 'r') as file:
        new_j_student_1 = json.load(file)

    new_student_1.reload_from_json(new_j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
