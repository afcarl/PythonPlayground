#!/bin/python

"""
Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
"""

__author__ = "Tarun Chhabra"
__copyright__ = "Copyright 2016"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Tarun Chhabra"
__status__ = "Development"


def has_duplicates(input_list):
    """
    :rtype: bool
    :param input_list: A list of values
    :return: returns True if there are any duplicate elements
    """
    if input_list is None:
        return False
    unique = set(input_list)
    if len(unique) == len(input_list):
        return False
    return True

print has_duplicates([1,2,3,4])
print has_duplicates('banana')
print has_duplicates([1.34,5.66,5.66])