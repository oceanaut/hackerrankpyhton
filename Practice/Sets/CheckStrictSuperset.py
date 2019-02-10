# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

#!/bin/python3

if __name__ == '__main__':
    # set1, count = set(input().split()), int(input())
    # print(not False in [set(input().split()) < set1 for _ in range(count)])
    a = set(input().split())
    print(a)
    print(all(a > set(input().split()) for _ in range(int(input()))))
