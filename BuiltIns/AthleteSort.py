#!/bin/python3

"""
https://www.hackerrank.com/challenges/python-sort-sort/problem
"""

if __name__ == '__main__':
    N, M = map(int, input().split())
    rows = [input() for _ in range(N)]
    K = int(input())

    for row in sorted(rows, key=lambda row: int(row.split()[K])):
        print(row)

