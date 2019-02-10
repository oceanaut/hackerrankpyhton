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
    print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')
    # print(*sorted(input(), key="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468".index), sep="")

