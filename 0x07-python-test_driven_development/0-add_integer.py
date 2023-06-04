#!/usr/bin/python3
"""
    0-add_integer: add_integer()
"""

def add_integer(a, b=98):
    """
        add_integer returns the sum of two integers
        Args:
            a: first number.
            b: second number.
        Returns:
            sum of the two integers
    """
    if (type(a) != float) and (type(a) != int):
        raise TypeError("a must be an integer")
    elif (type(b) != float) and (type(b) != int):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
