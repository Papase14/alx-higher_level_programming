#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    size = avg = 0
    for tupl in my_list:
        x, y = tupl
        size += (x * y)
        avg += y
    return size / avg
