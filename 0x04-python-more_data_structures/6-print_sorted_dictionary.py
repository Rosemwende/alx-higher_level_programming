#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    if a_dictionary:
        for x, y in a_dictionary.items():
            keys.append(x)

        keys.sort()
        for items in keys:
            print("{}: {}".format(items, a_dictionary[items]))
