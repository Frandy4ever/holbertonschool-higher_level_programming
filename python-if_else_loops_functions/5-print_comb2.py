#!/usr/bin/python3
# Loop through numbers from 0 to 99.
for number in range(0, 100):
    if number == 99:
        # If the current number is 99, print it without a comma.
        print("{}".format(number))
    else:
        # For all other numbers, print with leading zeros and a comma.
        print("{:02}".format(number), end=", ")
