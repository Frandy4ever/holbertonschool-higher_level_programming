#!/usr/bin/python3
# Import the 'random' module to generate random numbers.
import random

# Generate a random integer between -10000 and 10000 (inclusive).
number = random.randint(-10000, 10000)

# Calculate the last digit of the absolute value of 'number'.
digit = abs(number) % 10

# If 'number' is negative, make 'digit' negative as well.
if number < 0:
    digit = -digit

# Print the original number and its last digit.
print("Last digit of {} is {} and is ".format(number, digit), end="")

# Check the value of 'digit' and print an appropriate message.
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")