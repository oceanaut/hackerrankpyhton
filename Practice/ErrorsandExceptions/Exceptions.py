#!/bin/python3

"""
https://www.hackerrank.com/challenges/exceptions/problem
"""


if __name__ == '__main__':
    for i in range(int(input())):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except Exception as e:
            print("Error Code:", e)

