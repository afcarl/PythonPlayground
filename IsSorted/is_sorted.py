#!/bin/python

"""
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc.
"""

__author__ = "Tarun Chhabra"
__copyright__ = "Copyright 2016"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Tarun Chhabra"
__status__ = "Development"


def is_sorted(input_list):
    """
    :rtype: Boolean
    :param input_list: A list of numbers
    :return: True if input list is same as the original one
    """
    orig = input_list
    if orig == sorted(input_list):
        return True
    else:
        return False


# Test Cases

A = [11, 8, 5, 6, 10]

print is_sorted(A)

B = [1, 2, 3, 4, 5]

print is_sorted(B)
