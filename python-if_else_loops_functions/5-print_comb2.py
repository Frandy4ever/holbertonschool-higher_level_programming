#!/usr/bin/python3
# Loop through numbers from 0 to 99.
for number in range(100):
    if number == 99:
        # If the current number is 99, print it with two digits and a newline.
        print("{:02}\n".format(number), end="")
    else:
        # For all other numbers, print with two digits, a comma, and a space.
        print("{:02}, ".format(number), end="")