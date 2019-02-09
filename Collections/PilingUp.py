#!/bin/python3

from collections import deque

'''
https://www.hackerrank.com/challenges/piling-up/problem 
'''

if __name__ == '__main__':
    for _ in (range(int(input()))):
        input()
        side_lengths = deque(map(int, input().strip().split()))
        result = "Yes"
        if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
            result = "No"
        print(result)



