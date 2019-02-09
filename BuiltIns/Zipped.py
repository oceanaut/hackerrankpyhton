#!/bin/python3

"""
https://www.hackerrank.com/challenges/zipped/problem
"""

if __name__ == '__main__':
    n, x = map(int, input().split())
    sheet = []
    for _ in range(x):
        sheet.append(map(float, input().split()))
    for i in zip(*sheet):
        print(sum(i) / len(i))

