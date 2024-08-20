#!/usr/bin/python3
"""
Function to find a peak in a list of unsorted integers.
A peak is defined as an element that is greater than or equal to its neighbors.
"""
def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers.
    
    Args:
    list_of_integers (list): A list of unsorted integers.

    Returns:
    int: A peak element from the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    def peak_util(start, end):
        mid = (start + end) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return peak_util(start, mid - 1)
        else:
            return peak_util(mid + 1, end)

    return peak_util(0, len(list_of_integers) - 1)
