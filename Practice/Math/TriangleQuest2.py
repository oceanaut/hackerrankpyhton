# https://www.hackerrank.com/challenges/triangle-quest-2/problem

#!/bin/python3
import math

if __name__ == '__main__':
    for i in range(1, int(input()) + 1):
        print(((10 ** i - 1) // 9) ** 2)



