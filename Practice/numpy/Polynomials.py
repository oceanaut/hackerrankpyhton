#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-polynomials/problem
"""
# import numpy as np
# print(np.polyval(list(map(float,input().split())),float(input())))
print(__import__('numpy').polyval(list(map(float,input().split())),float(input())))
