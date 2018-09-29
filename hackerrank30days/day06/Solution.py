#!/bin/python3
#https://www.hackerrank.com/challenges/30-loops/problem

if __name__ == '__main__':
    for N in range(int(input())):
        S = input()
        print(S[::2], S[1::2])