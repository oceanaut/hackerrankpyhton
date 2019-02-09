#!/bin/python3

from collections import OrderedDict

'''
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
'''

if __name__ == '__main__':
    d = OrderedDict()
    for _ in range(int(input())):
        item, space, quantity = input().rpartition(' ')
        d[item] = d.get(item, 0) + int(quantity)
    for item, quantity in d.items():
        print(item, quantity)
    # print(*[" ".join([item, str(price)]) for item, price in d.items()], sep="\n")




