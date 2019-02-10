#!/bin/python3

from collections import namedtuple

'''
https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
'''

if __name__ == '__main__':
    (n, categories) = (int(input()), input().split())
    print(categories)
    Grade = namedtuple('Grade', categories)
    print(Grade)
    marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
    print((sum(marks) / len(marks)))



