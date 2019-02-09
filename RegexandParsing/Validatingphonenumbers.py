#!/bin/python3

"""
https://www.hackerrank.com/challenges/validating-the-phone-number/problem
"""
import re
# [print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]
for i in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):
        print('YES')
    else:
        print('NO')

