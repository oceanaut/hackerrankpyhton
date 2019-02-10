# https://www.hackerrank.com/challenges/py-set-mutations/problem

#!/bin/python3

if __name__ == '__main__':
    m = int(input())
    A = set(map(int, input().split()))
    n = int(input())

    for i in range(n):
        cmd, args = input().split()
        B = set(map(int, input().split()))
        eval('A.' + cmd + '(B)')
    print(sum(A))
