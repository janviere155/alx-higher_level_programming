#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # if the list is not empty
    if my_list is not None:
        # get the last index of the list
        l_idx = len(my_list) - 1
        # print the list in reverse order
        # starting from the last index
        for i in range(l_idx, -1, -1):
            print("{:d}".format(my_list[i]))
