#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""
import numpy
a=numpy.array(list(map(int,input().split())))
a.shape = (3, 3)
print(a)

