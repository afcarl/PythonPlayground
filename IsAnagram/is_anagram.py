#!/bin/python

"""
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""

__author__ = "Tarun Chhabra"
__copyright__ = "Copyright 2016"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Tarun Chhabra"
__status__ = "Development"


def is_anagram(str1, str2):
    """
    :rtype: bool
    :param str1: First string
    :param str2: Second string
    :return: True if the two strings are anagrams
    """
    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            return True
        else:
            return True
    else:
        return False


print is_anagram('life', 'elif')
print is_anagram('yes', 'no')
print is_anagram('naan', 'anna')
