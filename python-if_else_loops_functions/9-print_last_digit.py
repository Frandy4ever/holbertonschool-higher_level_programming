#!/usr/bin/python3
def print_last_digit(number):
    # Calculate and print the last digit of the absolute value of 'number'.
    print(abs(number) % 10, end="")

    # Return the last digit as an integer.
    return (abs(number) % 10)