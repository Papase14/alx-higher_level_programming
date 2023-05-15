#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_new = []
    for x in my_list:
        list_new.append(x % 2 == 0)
    return list_new
