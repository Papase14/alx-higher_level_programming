#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
  num_printed = 0
  try:
    for i in range(x):
      value = my_list[i]
      if type(value) == int:
        print("{:d}".format(value), end="")
        num_printed += 1
    print()
  except:
    pass
  return num_printed