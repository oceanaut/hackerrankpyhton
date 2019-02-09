#!/bin/python3

"""
https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""

import re


if __name__ == '__main__':
    for _ in range(int(input())):
        print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
