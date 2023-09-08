#!/usr/bin/python3
# Loop through the ASCII values of lowercase letters from 'a' to 'z'.
for letter in range(97, 123):
    # Convert the ASCII value to the corresponding lowercase letter and print it.
    print("{}".format(chr(letter)), end="")
    