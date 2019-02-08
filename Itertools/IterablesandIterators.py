#!/bin/python3


import itertools

'''
https://www.hackerrank.com/challenges/iterables-and-iterators/problem

'''

if __name__ == '__main__':
    N, list1, K = int(input()), input().split(), int(input())
    print(sum(['a' in i for i in list(itertools.combinations(list1, K))]) / len(list(itertools.combinations(list1, K))))



