#!/bin/python3

"""
https://www.hackerrank.com/challenges/validating-uid/problem
validating all the randomly generated UIDs.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def valid(s):
    if len(s) != 10:
        return 'Invalid'
    else:
        if  not re.search(r'.*[A-Z].*[A-Z].*', s):
            return 'Invalid'
        elif not re.search(r'.*\d.*\d.*\d.*', s):
            return 'Invalid'
        elif not re.search(r'[a-zA-Z\d]{10}', s):
            return 'Invalid'
        elif re.search(r'(.).*\1', s):
            return 'Invalid'
    return 'Valid'


if __name__ == '__main__':
    for _ in range(int(input())):
        print(valid(input()))
