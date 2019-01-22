# https://www.hackerrank.com/challenges/py-set-union/problem

#!/bin/python3

if __name__ == '__main__':
    x, a, y, b = [set(input().split()) for _ in '1234'];print(len(a & b))

