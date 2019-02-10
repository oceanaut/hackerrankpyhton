#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-arrays/problem
"""
import numpy


def arrays(arr_param):
    # complete this function
    # use numpy.array
    return(numpy.array(arr[::-1], float))


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

