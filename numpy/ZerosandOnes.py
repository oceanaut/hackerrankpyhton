#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
"""
import numpy
N = tuple(map(int, input().strip().split()))
z = numpy.zeros(N, dtype=numpy.int)
o = numpy.ones(N, dtype=numpy.int)
print(z)
print(o)
