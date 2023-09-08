#!/usr/bin/python3
# Loop through the ASCII values of lowercase letters ('a' to 'z').
for letter in range(97, 123):
    # Print the lowercase letter, formatting it as a string without a newline.
    print("{:c}".format(letter), end="")
