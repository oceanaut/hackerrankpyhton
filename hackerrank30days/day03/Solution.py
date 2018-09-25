#!/bin/python3

#https://www.hackerrank.com/challenges/30-conditional-statements/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N in range(1, 101):
        mod = N % 2
    if mod > 0: print("Weird")
    else:
        if N in range(2,6): print("Not Weird")
        if N in range(6,21): print("Weird")
        if N>20 : print("Not Weird")