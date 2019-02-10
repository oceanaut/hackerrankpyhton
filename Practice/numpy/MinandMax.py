#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-min-and-max/problem
"""
import numpy as np
print(np.max(np.min(np.array([input().split() for _ in range(int(input().split()[0]))],int),axis=1)))
