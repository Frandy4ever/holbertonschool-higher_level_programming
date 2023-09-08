#!/usr/bin/python3
# Loop through the ASCII values of lowercase letters ('a' to 'z').
for letter in range(ord('a'), ord('z') + 1):
    # Check if the current letter is not 'q' and not 'e'.
    if chr(letter) not in ['q', 'e']:
        # Print the lowercase letter without a newline.
        print("{}".format(chr(letter)), end="")
