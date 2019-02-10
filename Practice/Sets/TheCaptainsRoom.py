# https://www.hackerrank.com/challenges/py-the-captains-room/problem

#!/bin/python3

if __name__ == '__main__':
    k, arr = int(input()), list(map(int, input().split()))
    myset = set(arr)
    print(((sum(myset) * k) - (sum(arr))) // (k - 1))

