#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-eye-and-identity/problem
"""
import numpy
numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int,input().split())))
