#!/bin/python3

"""
https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
"""
import numpy as np
np.set_printoptions(sign=' ')
my_array = np.array(input().split(),float)
print(np.floor(my_array))
print(np.ceil(my_array))
print(np.rint(my_array))
