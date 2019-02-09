#!/bin/python3

"""
https://www.hackerrank.com/challenges/validating-credit-card-number/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1",
                                                                                    s.replace("-", "")):
            print("Valid")
        else:
            print("Invalid")
