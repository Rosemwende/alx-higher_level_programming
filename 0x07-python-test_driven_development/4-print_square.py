#!/usr/bin/python3
"""Module for printing a square with hashes"""

def print_square(size):
    """
    Function that prints a square with hashes (#)

    Args:
        size (int): Size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
