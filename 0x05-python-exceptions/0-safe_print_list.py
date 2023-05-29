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

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))