#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""
import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)],float)
numpy.set_printoptions(legacy='1.13') #important
print(numpy.linalg.det(a))
