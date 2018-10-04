#!/bin/python3

#Task
#Write a factorial function that takes a positive integer, as a parameter and prints the result of ( factorial).
#Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .
#https://www.hackerrank.com/challenges/30-recursion/problem

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n>1: return n*factorial(n-1)
    else: return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    if n in range (2,13):
        result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()