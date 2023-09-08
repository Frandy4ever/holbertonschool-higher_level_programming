#!/usr/bin/python3
for char_code in range(ord('z'), ord('A') - 1, -1):
    char = chr(char_code)
    # Check if the character is lowercase or uppercase and print accordingly.
    print(char.lower() if char.isupper() else char.upper(), end="")