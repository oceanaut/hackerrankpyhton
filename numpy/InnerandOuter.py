#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-inner-and-outer/problem
"""
import numpy as np
A,B = [np.array([input().split()],int) for _ in range(2)]
print(np.inner(A,B)[0][0],np.outer(A,B),sep="\n")
