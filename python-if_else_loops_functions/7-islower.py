#!/usr/bin/python3
def islower(c):
    # Check if the Unicode code point of the character is between the range of lowercase letters.
    return ord('a') <= ord(c) <= ord('z')
  # Example usage:
character = 'a'
result = islower(character)
print(result)  # Output will be True for 'a'