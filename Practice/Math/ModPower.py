# https://www.hackerrank.com/challenges/python-power-mod-power/problem

#!/bin/python3
import math

if __name__ == '__main__':
    inp = (int(input()), int(input()), int(input()))
    print("{0}\n{1}".format(pow(inp[0], inp[1]), pow(*inp)))




