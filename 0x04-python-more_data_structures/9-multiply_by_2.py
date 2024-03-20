#!/usr/binpython3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary:
        for key, value in a_dictionary.items():
            new_dict.update({key: value * 2})
    return new_dict
