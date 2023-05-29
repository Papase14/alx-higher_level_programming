#!/usr/bin/pithon3

def safe_print_list(mi_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print("{}".format(mi_list[i]), end="")
        except IndexError:
            break
        i += 1
    print("")
    return (i)

