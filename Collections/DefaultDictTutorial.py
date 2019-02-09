#!/bin/python3

from collections import defaultdict

'''
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, 
but the only difference is that a defaultdict will have a default value if that key has not been set yet.
'''

if __name__ == '__main__':
    d, n = defaultdict(list), list(map(int, input().split()))
    for i in range(n[0]):
        d[input()].append(i + 1)
    for i in range(n[1]):
        print(' '.join(map(str, d[input()])) or -1)

