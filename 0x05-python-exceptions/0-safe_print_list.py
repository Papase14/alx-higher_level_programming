#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for element in my_list[:x]:
            print(element, end="")
            elements_printed += 1
        print()
    except IndexError:
        pass
    return elements_printed
