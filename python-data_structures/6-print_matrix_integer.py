#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            print(f"{value:d}", end="")
            if j != (len(row) - 1):
                print(" ", end="")
        print("")
