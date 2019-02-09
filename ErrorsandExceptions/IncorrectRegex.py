#!/bin/python3

"""
https://www.hackerrank.com/challenges/incorrect-regex/problem
"""
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            print(bool(re.compile(input())))
        except:
            print('False')
