#!/bin/python3

"""
https://www.hackerrank.com/challenges/python-time-delta/problem
"""
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    tt1=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    tt2=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((tt1-tt2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + "\n")
    fptr.close()


