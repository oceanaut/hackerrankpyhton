#!/bin/python3

#Task
#Given a string, , of length that is indexed from to , print its even-indexed and odd-indexed characters as space-separated strings on a single line (see the Sample below for more detail).
#Note: is considered to be an even index.
#https://www.hackerrank.com/challenges/30-loops/problem

if __name__ == '__main__':
    for N in range(int(input())):
        S = input()
        print(S[::2], S[1::2])