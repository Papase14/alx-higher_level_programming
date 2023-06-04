#!/usr/bin/python3

def add_integer(a, b=98):
    if (type(a) != float) and (type(a) != int):
        raise TypeError("a must be an integer")
    elif (type(b) != float) and (type(b) != int):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)



print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)