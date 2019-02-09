#!/bin/python3

"""
https://www.hackerrank.com/challenges/any-or-all/problem
any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.
all()
This expression returns True if all of the elements of the iterable are true.
If the iterable is empty, it will return True
"""

if __name__ == '__main__':
    N, n = int(input()), input().split()
    print(all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n]))

