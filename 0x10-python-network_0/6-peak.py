#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """
    Finds the largest value in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: The largest value in the input list.
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
