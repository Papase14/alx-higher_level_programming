#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum = [0, 0]
    for x in range(2):
        if x < len(tuple_a):
            sum[x] += tuple_a[x]
        if x < len(tuple_b):
            sum[x] += tuple_b[x]
    return tuple(sum)
