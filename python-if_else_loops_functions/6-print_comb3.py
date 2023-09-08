#!/usr/bin/python3
# Loop through the first digit from 0 to 9.
for digit1 in range(0, 10):
    # Nested loop through the second digit from (digit1 + 1) to 9.
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            # If the current pair is 89, print it without a comma.
            print("{}{}".format(digit1, digit2))
        else:
            # For all other pairs, print with a comma and a space.
            print("{}{}".format(digit1, digit2), end=", ")