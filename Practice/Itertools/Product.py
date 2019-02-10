#!/bin/python3

from itertools import product

'''
https://www.hackerrank.com/challenges/itertools-product/problem
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
'''

if __name__ == '__main__':
    # A = list(map(int, input().split()))
    # B = list(map(int, input().split()))
    # print(list(product(A, B)))
    # A = map(int, input().split())
    # B = map(int, input().split())
    # print(*product(A, B))
    # A = map(int, input().split())
    # B = map(int, input().split())
    # print(list(product(A, B)))
    # print(list(product(list(map(int, input().split())), list(map(int, input().split())))))
    print(*product(list(map(int, input().split())), list(map(int, input().split()))))
