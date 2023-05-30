#!/usr/bin/python3

class Square:
    def __init__(self):
        pass


Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)