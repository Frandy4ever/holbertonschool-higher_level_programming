#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    counted_track = 0
    for indx in range(0, x):
        try:
            print("{:d}".format(my_list[indx]), end="")
            counted_track += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (counted_track)
