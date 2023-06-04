#!/usr/bin/python3
"""
    4-print_square: print_square()
"""

def print_square(size):
    """
        print_square prints square of size provided.
        Args:
            size (int): size of square.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
