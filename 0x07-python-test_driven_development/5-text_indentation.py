#!/usr/bin/python3
#5-text_indentation.py
"""Module for printing a text with new lines after certain characters"""

def text_indentation(text):
    """Prints text with new lines after '.', '?' and ':'
    Args:
    text (str): The text to be indented"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    start = 0
    for i, char in enumerate(text):
        if char in separators:
            print(text[start:i + 1].strip() + '\n')
            if i + 1 < len(text) and text[i + 1] == ' ':
                start = i + 2
            else:
                start = i + 1
    print(text[start:].strip(), end="")
