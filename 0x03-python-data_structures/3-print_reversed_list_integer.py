#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
        list = my_list.reverse()
        for i in list:
            print("{:d}".format(i))
