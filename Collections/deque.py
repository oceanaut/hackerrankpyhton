#!/bin/python3

from collections import deque

'''
https://www.hackerrank.com/challenges/py-collections-deque/problem
A deque is a double-ended queue. It can be used to add or remove elements from both ends. 
'''

if __name__ == '__main__':
    d = deque()
    for _ in range(int(input())):
        inp = input().split()
        getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    print(*[item for item in d])



