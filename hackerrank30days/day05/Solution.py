#!/bin/python3


#Task
#Given an integer, , print its first multiples. Each multiple (where ) should be printed on a new line in the form: n x i = result.
#https://www.hackerrank.com/challenges/30-loops/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n in range(2,21):
        for i in range(1,11):
            s=input()
            print( )