# https://www.hackerrank.com/challenges/python-mod-divmod/problem

#!/bin/python3
import math

if __name__ == '__main__':
    # A = int(input()); B = int(input());print(A//B);print(A%B);print(divmod(A, B))
    # print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))
    print(*divmod(177, 10))
    print('{0}\n{1}\n({0}, {1})'.format(*divmod(177, 10)))
    # a = int(input()); b = int(input())
    # print(a // b, a % b, divmod(a, b), sep='\n')
    # a, b = int(input()), int(input())
    # print("{d[0]}\n{d[1]}\n{d}".format(d=divmod(a, b)))



