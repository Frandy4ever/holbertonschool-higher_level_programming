#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    counted_track = 0
    for indx in range(x):
        try:
            print("{}".format(my_list[indx]), end="")
            counted_track += 1
        except IndexError:
            break
    print("")
    return (counted_track)
