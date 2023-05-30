#!/usr/bin/python3
''' Module 4-square: class Square '''

class Square():
    ''' class square that defones a square '''
    def __init__(self, size=0):
        ''' Initialises a new square with a size '''

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        ''' getter function for private attribute size. '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' setter function for private attribute size. '''
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' area of the square. '''
        return self.__size * self.__size