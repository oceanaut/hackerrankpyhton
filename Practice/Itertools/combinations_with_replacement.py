#!/bin/python3

from itertools import combinations_with_replacement

'''
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
'''

if __name__ == '__main__':
    S, k = input().split()
    print('\n'.join([''.join(c) for c in combinations_with_replacement(sorted(S), int(k))]))




