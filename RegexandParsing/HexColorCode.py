#!/bin/python3

"""
https://www.hackerrank.com/challenges/hex-color-code/problem
"""
import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]
