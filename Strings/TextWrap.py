#https://www.hackerrank.com/challenges/text-wrap/problem

#!/bin/python3

import textwrap

if __name__ == '__main__':
    s = input().strip()
    n=int(input())
    print(textwrap.fill(s,n))

