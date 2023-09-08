#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Use list comprehension to convert command-line arguments to integers and sum them.
    total = sum(int(arg) for arg in sys.argv[1:])

    print(total)
