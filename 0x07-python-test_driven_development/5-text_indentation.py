#!/usr/bin/python3
"""
Module for text indentation.
"""

def text_indentation(text):
    """
    Function that prints a text with 2 new lines after '.', '?' and ':' characters

    Args:
        text (str): Input text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, "{}\n\n".format(char))

    print(text)
