#!/bin/python3

#Task
#Given an array, , of integers, print 's elements in reverse order as a single line of space-separated numbers.
#https://www.hackerrank.com/challenges/30-arrays/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(' '.join(str(x) for x in arr[::-1]))