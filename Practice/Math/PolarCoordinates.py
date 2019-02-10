# https://www.hackerrank.com/challenges/polar-coordinates/problem

#!/bin/python3

import cmath

if __name__ == '__main__':
    r = complex(input().strip())
    print(cmath.polar(r)[0])
    print(cmath.polar(r)[1])

