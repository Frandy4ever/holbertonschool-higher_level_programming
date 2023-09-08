#!/usr/bin/python3
# Loop through the ASCII values of lowercase letters ('a' to 'z').
for letter in range(ord('a'), ord('z') + 1):
    # Print the lowercase letter, formatting it as a string without a newline.
    print("{}".format(chr(letter)), end="")
