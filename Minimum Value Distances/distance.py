#!/bin/python

"""
Consider an array of  integers, A = [a1,a2, ...., an] . The distance between two indices, i  and , j is denoted by .
d[i,j] =

Given A, find the minimum d[i,j] such that A[i] = A[j] and . In other words, find the minimum distance between any
pair of equal elements in the array. If no such value exists, print .

Input Format

The first line contains an integer , n , denoting the size of array .
The second line contains n space-separated integers describing the respective elements in array A.

Constraints:

1 <= n <= 10^3
1 <= A[i] <= 10^5


Output Format

Print a single integer denoting the minimum  in ; if no such value exists, print -1 .

"""

__author__ = "Tarun Chhabra"
__copyright__ = "Copyright 2016"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Tarun Chhabra"
__status__ = "Development"

n = int(raw_input().strip())
A = map(int, raw_input().strip().split(' '))
d = {}
index = 0
minimum = n + 1
for i in A:
    if d.get(i) is None:
        d[i] = index
    else:
        d[i] = index - d[i]
        if d[i] < minimum:
            minimum = d[i]
    index += 1
if minimum == n + 1:
    minimum = -1
print minimum
