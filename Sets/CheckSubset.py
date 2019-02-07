# https://www.hackerrank.com/challenges/py-check-subset/problem

#!/bin/python3

if __name__ == '__main__':
    for _ in range(int(input())):
        _, A = int(input()), set(map(int, input().split()))
        _, B = int(input()), set(map(int, input().split()))
        print(A.issubset(B))

