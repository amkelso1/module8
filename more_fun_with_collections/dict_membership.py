"""
Author: Alex Kelso
Date: 10/20/2020
program: dict_membership.py.py

purpose: create and test a dictionary
"""


def in_dict():
    x = {'a', 'b', 'c'}
    y = input()
    if y in x:
        print(True)
    else:
        print(False)
    return x


in_dict()
