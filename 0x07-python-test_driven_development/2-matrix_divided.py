#!/usr/bin/python3

"""Module for dividing elements of a matrix"""

def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix by a divisor

    Args:
        matrix (list of lists): Matrix of integers/floats
        div (int or float): Divisor

    Returns:
        list of lists: New matrix with elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists, or if div is not an int or float
        ValueError: If matrix is empty or if div is zero
        """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix or not all(matrix):
        raise ValueError("matrix can't be empty")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)
    return new_matrix
