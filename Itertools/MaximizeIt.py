#!/bin/python3


from itertools import product

'''
https://www.hackerrank.com/challenges/maximize-it/problem

'''

if __name__ == '__main__':
    K, M = map(int, input().split())
    N = (list(map(int, input().split()))[1:] for _ in range(K))
    print(max((sum(num ** 2 for num in numbers) % M for numbers in product(*N))))

