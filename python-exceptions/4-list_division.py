#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for indx in range(0, list_length):
        try:
            quotient = my_list_1[indx] / my_list_2[indx]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)
    return (new_list)
