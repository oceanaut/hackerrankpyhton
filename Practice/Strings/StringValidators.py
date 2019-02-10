#https://www.hackerrank.com/challenges/string-validators/problem

#!/bin/python3

if __name__ == '__main__':
    s = input().strip()
    if len(s) in range(1,1001):
        for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
            print(any(method(c) for c in s))

