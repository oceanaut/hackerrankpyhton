#!/bin/python3

from itertools import combinations

'''
https://www.hackerrank.com/challenges/itertools-combinations/problem
Permutations are printed in a lexicographic sorted order. 
So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
'''

if __name__ == '__main__':
    S, n = input().split()
    for i in range(1, int(n)+1):
        print('\n'.join([''.join(c) for c in combinations(sorted(S), int(i))]))
    # s, n = input().split()
    # print("\n".join([(''.join(p)) for i in range(1, int(n)+1) for p in combinations(sorted(s), i)]))



