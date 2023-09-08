#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add  # Import the 'add' function from the 'add_0' module.

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))  # Calculate and print the sum of 1 and 2 using the 'add' function.

