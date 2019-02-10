#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-dot-and-cross/problem
matrices multiplication is dot product of them.
"""
import numpy
n= int(input())
a = numpy.array([input().split() for _ in range(n)],int)
b = numpy.array([input().split() for _ in range(n)],int)
print(numpy.dot(a,b))
