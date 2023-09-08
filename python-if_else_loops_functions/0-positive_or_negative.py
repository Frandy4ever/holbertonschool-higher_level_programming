#!/usr/bin/python3
import random  # Import the random module
# Generate a random integer between -10 and 10 (inclusive)
number = random.randint(-10, 10)
# Check the value of 'number' and print the appropriate message
if number > 0:
    print(number + " is positive")
elif number == 0:
    print(number + " is zero")
else:
    print(number + " is negative")