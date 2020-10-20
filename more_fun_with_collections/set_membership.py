"""
Author: Alex Kelso
Date: 10/19/2020
program: set_membership.py

purpose: Demonstrate use of a set
"""


def in_set():
    my_set = set('b')
    print(my_set)
    x = input()
    if x in my_set:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    in_set()

