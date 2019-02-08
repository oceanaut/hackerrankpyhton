#!/bin/python3

from itertools import permutations

'''
https://www.hackerrank.com/challenges/itertools-permutations/problem
Permutations are printed in a lexicographic sorted order. 
So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
'''

if __name__ == '__main__':
    S, k = input().split()
    # for c in permutations(sorted(S), int(k)):
    #     print(''.join(c))
    # print(''.join([''.join(i) for i in list(permutations(sorted(S), int(k)))]))
    # print([''.join(c) for c in permutations(sorted(S), int(k))])
    print('\n'.join([''.join(c) for c in permutations(sorted(S), int(k))]))
    # print('\n'.join([''.join(i) for i in list(permutations(sorted(S), int(k)))]))


