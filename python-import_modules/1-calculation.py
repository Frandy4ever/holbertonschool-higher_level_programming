#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, product, and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div  # Import the 'add', 'sub', 'mul', and 'div' functions from the 'calculator_1' module.

    a = 10
    b = 5

    # Perform arithmetic operations and print the results.
    print("{} + {} = {}".format(a, b, add(a, b)))  # Calculate and print the sum of 10 and 5 using the 'add' function.
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Calculate and print the difference of 10 and 5 using the 'sub' function.
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Calculate and print the product of 10 and 5 using the 'mul' function.
    print("{} / {} = {}".format(a, b, div(a, b)))  # Calculate and print the quotient of 10 and 5 using the 'div' function.
