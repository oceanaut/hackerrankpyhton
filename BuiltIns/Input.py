#!/bin/python3

"""
https://www.hackerrank.com/challenges/input/problem
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

"""

if __name__ == '__main__':
    ui = input().split()
    x = int(ui[0])
    print(eval(input()) == int(ui[1]))

