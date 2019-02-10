#!/bin/python3

"""
https://www.hackerrank.com/challenges/matrix-script/problem
"""

import re
import sys
print(re.sub(r"\b(?<=[A-Z1-9a-z])[^A-Z1-9a-z]+\b"," ","".join(map(lambda x : "".join(x),zip(*sys.stdin.read().split("\n")[1:])))))
