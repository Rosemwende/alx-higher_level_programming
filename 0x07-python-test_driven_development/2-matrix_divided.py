#!/usr/bin/python3
#2-matrix_divided.py
"""Module for dividing all elements of a matrix"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
    matrix: The matrix to divide
    div (int/float): The divisor
    Returns new matrix with elements divided by div"""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
