#!/usr/bin/python3
if __name__ == "__main__":
    import sys  # Import the 'sys' module, which provides access to command-line arguments.

    count = len(sys.argv) - 1  # Calculate the number of command-line arguments provided, excluding the script name.

    if count == 0:
        print("0 arguments.")  # If no arguments are provided (excluding the script name), print "0 arguments."
    elif count == 1:
        print("1 argument:")  # If only one argument is provided (excluding the script name), print "1 argument:"
    else:
        print("{} arguments:".format(count))  # If more than one argument is provided, print the count followed by "arguments:"

    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))  # Print each argument along with its position (index + 1).
