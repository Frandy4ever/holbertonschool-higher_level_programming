#!/usr/bin/python3
# Import the 'random' module to generate random numbers.
import random

# Generate a random integer between -10 and 10 (inclusive).
number = random.randint(-10, 10)

# Check the value of 'number' and print an appropriate message.
if number > 0:
    # If 'number' is greater than 0, it's considered positive.
    print("{} is positive".format(number))
elif number == 0:
    # If 'number' is equal to 0, it's considered zero.
    print("{} is zero".format(number))
else:
    # If 'number' is less than 0, it's considered negative.
    print("{} is negative".format(number))
