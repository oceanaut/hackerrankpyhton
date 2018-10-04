#!/bin/python3

#Task
#Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum
#number of consecutive 's in 's binary representation.
#https://www.hackerrank.com/challenges/30-binary-numbers/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print(max(len(length) for length in bin(int(input().strip()))[2:].split('0')))


