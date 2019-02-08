#!/bin/python3

from itertools import groupby

'''
https://www.hackerrank.com/challenges/compress-the-string/problem
You are given a string . Suppose a character '' occurs consecutively times in the string. 
Replace these consecutive occurrences of the character '' with in the string. 
'''

if __name__ == '__main__':
    print(*[(len(list(c)), int(k)) for k, c in groupby(input())])




