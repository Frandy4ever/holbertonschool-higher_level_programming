#!/usr/bin/python3
if __name__ == "__main__":
    # Print all non-private names defined by hidden_4 module.
    import hidden_4

    # Filter out names that start with double underscores and print the rest.
    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)
