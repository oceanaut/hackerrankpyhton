#!/bin/python3

from collections import Counter, OrderedDict

'''
https://www.hackerrank.com/challenges/word-order/problem
'''

if __name__ == '__main__':
    class OrderedCounter(Counter, OrderedDict):
        pass
    d = OrderedCounter(input() for _ in range(int(input())))
    print(len(d))
    print(*d.values())




