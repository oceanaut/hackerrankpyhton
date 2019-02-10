#!/bin/python3

from collections import Counter

'''
https://www.hackerrank.com/challenges/collections-counter/problem
'''

if __name__ == '__main__':
    numShoes, stock = input(), Counter(list(map(int, input().split())))
    print()
