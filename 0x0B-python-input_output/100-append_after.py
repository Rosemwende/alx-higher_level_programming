#!/usr/bin/python3
"""This module defines a function that appends a line of text after each line containing
a specific string in a file"""

def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string"""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
