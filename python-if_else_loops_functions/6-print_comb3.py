#!/usr/bin/python3
# Loop through the first digit from 0 to 9.
for digit1 in range(10):
    # Nested loop through the second digit from 0 to 9.
    for digit2 in range(10):
        # Check if the two digits are different and the first digit is less than the second.
        if digit1 != digit2 and digit1 < digit2:
            # Print the smallest combination of two different digits.
            print("{:02}, ".format(digit1 * 10 + digit2), end="")
print('')