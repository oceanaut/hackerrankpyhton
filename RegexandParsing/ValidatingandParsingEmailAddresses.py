#!/bin/python3

"""
https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
"""
import re
for _ in range(int(input())):
    x, y = input().split()
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y):
        print(x,y)

