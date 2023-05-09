#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

result = str("Last digit of {0}".format(number), end=" ")
#last_digit = int(repr(number)[-1])

if last_digit > 5:
    print(result + " is {0} and is greater than 5".format(last_digit))
elif last_digit == 0:
    print(result + " is {0} and is 0".format(last_digit))
else:
    print(result + " is {0} and is less than 6 and not 0".format(last_digit))
