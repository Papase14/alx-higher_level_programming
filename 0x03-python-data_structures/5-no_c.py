#!/usr/bin/python3

def no_c(my_string):
    string = my_string.translate({ord(x): None for x in 'cC'})
    return string
