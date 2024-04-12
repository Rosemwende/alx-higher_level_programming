#!/usr/bin/python
"""
Module for matrix multiplication.
"""

def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        list of lists: Resultant matrix

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or if elements are not integers/floats
        ValueError: If m_a or m_b is empty or if matrices can't be multiplied
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not m_a or not m_b:
        raise ValueError("m_a or m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(m_a_row, m_b_col)) for m_b_col in zip(*m_b)] for m_a_row in m_a]
    return result
