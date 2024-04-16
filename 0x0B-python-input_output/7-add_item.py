#!/usr/bin/python3
"""Adds all arguments to a Python list, then saves them to a file"""

import sys
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)
